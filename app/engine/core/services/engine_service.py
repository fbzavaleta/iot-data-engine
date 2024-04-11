from app.engine.core.lib.engine_response import EngineResponse
from app.engine.core.enums.engine import EngineEndpoint
from app.engine.core.enums.engine import (
    ErrorCode,
    ErrorMessage,
    EngineErrors,
    SucessCode,
    SucessMessage,
    EngineSuccess,
)
from app.engine.core.enums.common import ApiNotes
from app.engine.core.database import db_handler
from app.engine.core.database.db_model import Models
from flask import Request

from functools import lru_cache as memoized
from dataclasses import asdict

"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""


class EngineService:
    def __init__(self, request: Request = None) -> None:
        session = db_handler.DBConnectionPoolSingleton.get_instance().Session
        engine = db_handler.MysqlEngine(session)
        self.sql_engine = engine
        self.engine_response = EngineResponse(request)

    @property
    @memoized(maxsize=1)
    def register_endpoint(
        self,
    ) -> bool:
        endpoint_config = EngineEndpoint(**self.engine_response.fetch_query_parameters)
        if not endpoint_config:
            return EngineErrors(
                ErrorCode.INVALID_INPUTS, ErrorMessage.INVALID_INPUTS
            ).to_dict

        if not endpoint_config.channel:
            return EngineErrors(
                ErrorCode.CHANNEL_NOT_FOUND, ErrorMessage.CHANNEL_NOT_FOUND
            ).to_dict

        db_operation = self.sql_engine.insert_row(
            Models().EngineEndpoint, asdict(endpoint_config)
        )
        if not db_operation:
            return EngineErrors(
                ErrorCode.DATABASE_ERROR, ErrorMessage.DATABASE_ERROR
            ).to_dict

        return EngineSuccess(
            SucessCode.ENDPOINT_REGISTRATION, SucessMessage.ENDPOINT_REGISTRATION
        ).to_dict

    @property
    @memoized(maxsize=1)
    def get_api_notes(self) -> dict:
        return asdict(ApiNotes())
