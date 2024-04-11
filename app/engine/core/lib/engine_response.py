from functools import lru_cache as memoized
from typing import Dict, Union
import ast
from flask import Request

from app.engine.core.enums.engine import EngineEndpoint

"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""


class EngineResponse:
    def __init__(self, request: Request) -> None:
        self.request = request

    @property
    @memoized(maxsize=1)
    def fetch_query_parameters(self) -> Union[Dict, None]:
        if not self.get_query_parameters:
            return None
        return self.get_query_parameters.to_dict()

    @property
    @memoized(maxsize=1)
    def fetch_body_data(self) -> Union[Dict, None]:
        try:
            return self.bytes2dict(self.get_body_data)
        except:
            return None

    @property
    @memoized(maxsize=1)
    def get_query_parameters(self) -> dict:
        return self.request.args

    @property
    @memoized(maxsize=1)
    def get_body_data(self) -> bytes:
        return self.request.get_data()

    @staticmethod
    def bytes2dict(data: bytes) -> Dict:
        decoded_data = data.decode("UTF-8")
        return ast.literal_eval(decoded_data)
