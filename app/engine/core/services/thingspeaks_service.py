from functools import lru_cache as memoized
from typing import Dict, Union, Iterator
from flask import Request
from app.engine.core.lib.thingspeaks_response import ThingSpeaksRequestResponse
from app.engine.core.lib.engine_response import EngineResponse
from app.engine.core.enums.engine import (
    ErrorCode,
    ErrorMessage,
    EngineErrors,
    SucessCode,
    SucessMessage,
    EngineSuccess,
    EndpointDescription,
    EndpointDescriptionField,
    EngineDataSample,
)
from app.engine.core.enums.thingspeaks import ApiParameters, ApiChannelResponse
from app.engine.core.database import db_handler
from app.engine.core.database.db_model import Models


"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""


class ThingSpeaksService:
    def __init__(self, request: Request = None) -> None:
        session = db_handler.DBConnectionPoolSingleton.get_instance().Session
        engine = db_handler.MysqlEngine(session)
        self.sql_engine = engine
        self.endpoint_table = Models().EngineEndpoint
        self.endpoint_description_table = Models().EngineEndpointDescription
        self.endpoint_description_field_table = Models().EngineEndpointDescriptionField
        self.sample_table = Models().EngineDataSample
        self.engine_response = EngineResponse(request)
        self.api_parameters = self._get_api_parameters
        self.new_rows = 0

    @property
    @memoized(maxsize=1)
    def ingest_channel_description(self) -> dict:
        if not self.api_parameters:
            return EngineErrors(
                ErrorCode.INVALID_INPUTS, ErrorMessage.INVALID_INPUTS
            ).to_dict
        tks_client = ThingSpeaksRequestResponse(
            self.api_parameters.channel_id,
            self.api_parameters.api_key,
            self.api_parameters.n_rows,
            self.api_parameters.interval,
        )
        channel_description_response = tks_client.get_channel_response

        if not self._skip_ingest_descriptions:
            desciptions_row = self.populate_descriptions_row(
                channel_description_response
            )
            db_operation = self.sql_engine.insert_row(
                self.endpoint_description_table, desciptions_row.to_dict
            )
            if not db_operation:
                return EngineErrors(
                    ErrorCode.DATABASE_ERROR, ErrorMessage.DATABASE_ERROR
                ).to_dict
            description_id = self.sql_engine.select_one(
                self.endpoint_description_table,
                [self.endpoint_description_table.id.name],
                self.endpoint_description_table.engine_endpoint_id.name,
                self.api_parameters.endpoint_id,
            )
            rows_description_field = self.populate_descriptions_field_row(
                channel_description_response
            )
            rows_description_field.engine_endpoint_description_id = description_id[0]

            db_operation = self.sql_engine.insert_row(
                self.endpoint_description_field_table, rows_description_field.to_dict
            )
            if not db_operation:
                return EngineErrors(
                    ErrorCode.DATABASE_ERROR, ErrorMessage.DATABASE_ERROR
                ).to_dict

        if not self._skip_ingest_feed(channel_description_response.last_entry_id):
            if self.new_rows > 0:
                self.api_parameters.n_rows = self.new_rows
                tks_client = ThingSpeaksRequestResponse(
                    self.api_parameters.channel_id,
                    self.api_parameters.api_key,
                    self.api_parameters.n_rows,
                    self.api_parameters.interval,
                )
            ingest_operation = self._ingest_feed(tks_client.get_feed_response)
            if not ingest_operation:
                return EngineErrors(
                    ErrorCode.DATABASE_ERROR, ErrorMessage.DATABASE_ERROR
                ).to_dict
            self.new_rows = 0
            return EngineSuccess(
                SucessCode.INGESTION_SUCCESS, SucessMessage.INGESTION_SUCCESS
            ).to_dict

        return EngineSuccess(SucessCode.NO_NEW_DATA, SucessMessage.NO_NEW_DATA).to_dict

    def populate_descriptions_row(
        self, tks_response: ApiChannelResponse
    ) -> EndpointDescription:
        endpoint_desc_row = EndpointDescription()
        endpoint_desc_row.engine_endpoint_id = self.api_parameters.endpoint_id
        endpoint_desc_row.channel_name = tks_response.name
        endpoint_desc_row.latitude = tks_response.latitude
        endpoint_desc_row.longitude = tks_response.longitude
        endpoint_desc_row.elevation = tks_response.elevation
        return endpoint_desc_row

    def populate_descriptions_field_row(
        self, tks_response: ApiChannelResponse
    ) -> EndpointDescriptionField:
        endpoint_desc_field_row = EndpointDescriptionField()
        endpoint_desc_field_row.field1_name = tks_response.field1
        endpoint_desc_field_row.field2_name = tks_response.field2
        endpoint_desc_field_row.field3_name = tks_response.field3
        endpoint_desc_field_row.field4_name = tks_response.field4
        endpoint_desc_field_row.field5_name = tks_response.field5
        endpoint_desc_field_row.field6_name = tks_response.field6
        endpoint_desc_field_row.field7_name = tks_response.field7
        endpoint_desc_field_row.field8_name = tks_response.field8

        return endpoint_desc_field_row

    @property
    @memoized(maxsize=1)
    def _get_api_parameters(self) -> Union[ApiParameters, None]:
        parameters = ApiParameters(**self.engine_response.fetch_body_data)
        channel_id = self.engine_response.fetch_query_parameters.get("channel")

        if not parameters and not channel_id:
            return None

        endpoint_id_token = self._get_endpoint_token_id(channel_id)
        parameters.channel_id = channel_id
        parameters.endpoint_id, parameters.api_key = endpoint_id_token.values()

        return parameters

    def _get_endpoint_token_id(self, channel_id: str) -> dict:
        data = self.sql_engine.select_one(
            self.endpoint_table,
            [self.endpoint_table.id.name, self.endpoint_table.token.name],
            self.endpoint_table.channel.name,
            channel_id,
        )
        return {"endpoint_id": data[0], "api_key": data[1]}

    @property
    @memoized(maxsize=1)
    def _get_endpoint_description_id(self) -> Union[int, None]:
        data = self.sql_engine.select_one(
            self.endpoint_description_table,
            [self.endpoint_description_table.id.name],
            self.endpoint_description_table.engine_endpoint_id.name,
            self.api_parameters.endpoint_id,
        )
        return data[0] if data else None

    @property
    @memoized(maxsize=1)
    def _skip_ingest_descriptions(self) -> bool:
        if self._get_endpoint_description_id:
            return True
        return False

    def _skip_ingest_feed(self, last_entry) -> bool:
        data = self.sql_engine.select_one(
            self.sample_table,
            [self.sample_table.entry_id.name],
            self.sample_table.engine_endpoint_id.name,
            self.api_parameters.endpoint_id,
            fetchall=True,
        )

        last_entry_db = max(data)[0] if data else None

        if not last_entry_db:  # there is no any data in the table for these channel
            return False
        if last_entry_db < last_entry:  # there new data arrived
            self.new_rows = last_entry - last_entry_db
            return False
        return True  # there is no new data

    def _ingest_feed(self, feed_generator: Iterator[Dict]) -> None:
        for feed in feed_generator:
            format_row = EngineDataSample(**feed)
            format_row.engine_endpoint_id = self.api_parameters.endpoint_id
            format_row.created_at = self._get_datetime(format_row.created_at)
            db_operation = self.sql_engine.insert_row(
                self.sample_table, format_row.to_dict
            )
            if not db_operation:
                return False
        return True

    def _get_datetime(
        self, datetime_string: str
    ) -> str:  # TODO: This should be included in a helper class
        return datetime_string.replace("Z", "+00:00")
