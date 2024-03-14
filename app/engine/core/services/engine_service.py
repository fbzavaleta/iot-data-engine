from engine.core.response.engine_response import EngineResponse
from engine.core.enums.engine import EngineEndpoint
from engine.core.enums.common import ApiNotes
from engine.core.database import db_handler, db_model

from functools import lru_cache as memoized
from dataclasses import asdict
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

class EngineService:
    def __init__(self, channel: str=None, token: str=None) -> None:
        self.channel = channel
        self.token = token
    
    @property
    @memoized(maxsize=1)
    def register_endpoint(self) -> bool:
        sucess = False
        row = EngineEndpoint(channel=self.channel, token=self.token)
        db_operation = db_handler.MysqlEngine().get_row(db_model.EngineEndpoint, asdict(row))
        if db_operation:
            sucess = True
        return sucess
    
    @property
    @memoized(maxsize=1)
    def get_api_notes(self) -> dict:
        return asdict(ApiNotes())