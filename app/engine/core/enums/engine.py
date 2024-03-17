from dataclasses import dataclass
from typing import Optional
from enum import Enum
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

@dataclass(frozen=False)
class EngineEndpoint:
    channel: str = None
    token: str = None

    def __init__(self, channel: Optional[str] = None, token: Optional[str] = None, **kwargs) -> None:
        self.channel = channel
        self.token = token

class ErrorCode(Enum):
    INVALID_INPUTS = 1
    CHANNEL_NOT_FOUND = 2
    CHANNEL_NOT_PUBLIC = 3
    DATABASE_ERROR = 4

@dataclass(frozen=False)
class ErrorMessage:
    INVALID_INPUTS = "Required Input parameters are not valid or missing"
    CHANNEL_NOT_FOUND = "Channel not found, please verify the channel id"
    CHANNEL_NOT_PUBLIC = "Channel is not public, you need to insert a valid token to access the channel"
    DATABASE_ERROR = "Database error, please contact the administrator"

@dataclass(frozen=False)
class EngineErrors:
    error_code: ErrorCode
    error_msg: ErrorMessage

    @property
    def to_dict(self):
        return {'error_code': self.error_code.value, 'error_msg': self.error_msg}
    
class SucessCode(Enum):
    ENDPOINT_REGISTRATION = 1

@dataclass(frozen=False)
class SucessMessage:
    ENDPOINT_REGISTRATION = "Endpoint registered successfully"

@dataclass(frozen=False)
class EngineSuccess:
    sucess_code: SucessCode
    sucess_msg: SucessMessage

    @property
    def to_dict(self):
        return {'error_code': self.sucess_code.value, 'error_msg': self.sucess_msg}    