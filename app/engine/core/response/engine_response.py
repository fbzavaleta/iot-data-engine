from functools import lru_cache as memoized
from typing import Dict, List, Union, Iterator
import ast
from werkzeug.datastructures import ImmutableMultiDict

from engine.core.enums.engine import EngineEndpoint
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

class EngineResponse:    
    @memoized(maxsize=1)
    def fetch_query_parameters(self, query_parameters: 
                               ImmutableMultiDict) -> Union[Dict, EngineEndpoint]:
        if not query_parameters:
            return {}
        return EngineEndpoint(**query_parameters.to_dict())
    
    @memoized(maxsize=1)
    def fetch_body_data(self, body_data: bytes) -> Dict:
        return self.bytes2dict(body_data)
    
    @staticmethod
    def bytes2dict(data: bytes) -> Dict:
        decoded_data = data.decode('UTF-8')
        return ast.literal_eval(decoded_data)