from functools import lru_cache as memoized
from typing import Dict, List, Union, Iterator
from flask import Request
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

class EngineResponse:
    def __init__(self, request: Request) -> None:
        self.query_parameters = request.args.to_dict()
    
    @property
    @memoized(maxsize=1)
    def validate_query_parameters(self) -> bool:
        print(self.query_parameters)
        return True