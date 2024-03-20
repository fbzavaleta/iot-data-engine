from engine.core.lib.thingspeaks_response import ThingSpeaksRequestResponse
from engine.core.lib.engine_response import EngineResponse
from engine.core.enums.engine import (
    ErrorCode, ErrorMessage, EngineErrors,
    SucessCode, SucessMessage, EngineSuccess)
from engine.core.enums.thingspeaks import ApiParameters
from engine.core.database import db_handler
from engine.core.database.db_model import Models
from flask import Request
from typing import Dict, Union

from functools import lru_cache as memoized
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

class ThingSpeaksService:
    def __init__(self, request: Request=None) -> None:
        self.engine_response = EngineResponse(request)

    @property
    @memoized(maxsize=1)
    def ingest_channel_description(self) -> dict:
        api_parameters = self._get_api_parameters

        if not api_parameters:
            return EngineErrors(ErrorCode.INVALID_INPUTS, ErrorMessage.INVALID_INPUTS).to_dict
        print(f"api_parameters: {api_parameters}") #FIXME: Remove this line
        
        #if channel_description:
        #    db_handler.MysqlEngine().insert_row(db_model.Channel, channel_description)
        #    return jsonify({'status': HttpStatus.OK, 'message': 'Channel description ingested'})
        #return jsonify({'status': HttpStatus.NOT_FOUND, 'message': 'Channel not found'})
        return {}
    
    @property
    @memoized(maxsize=1)
    def _get_api_parameters(self) -> Union[ApiParameters, None]:
        parameters = ApiParameters(**self.engine_response.fetch_body_data)
        channel_id = self.engine_response.fetch_query_parameters.get('channel')

        if not parameters and not channel_id:
            return None
        
        endpoint_id_token = self._get_endpoint_token_id(channel_id)
        parameters.channel_id = channel_id
        parameters.endpoint_id, parameters.token = endpoint_id_token.values()

        return parameters

    @property
    @memoized(maxsize=1)
    def _get_channel_feed(self):
        return self.request_response.fetch_body_data
    
    @memoized(maxsize=1)
    def _get_endpoint_token_id(self, channel_id: str)-> dict:
        endpoint = Models().EngineEndpoint
        sql_engine = db_handler.MysqlEngine()
        data = sql_engine.select_one(endpoint,
                                     [endpoint.id.name, endpoint.token.name],
                                     endpoint.channel.name, channel_id)
        return {'endpoint_id': data[0], 'api_key': data[1]}
