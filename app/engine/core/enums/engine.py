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

    @property #TODO: This should be a decorator
    def to_dict(self):
        return {'sucess_code': self.sucess_code.value, 'sucess_msg': self.sucess_msg}
    
@dataclass(frozen=False)
class EndpointDescription:
    engine_endpoint_id: int = None
    channel_name: str = None
    latitude: float = None
    longitude: float = None
    elevation: float = None

    @property #TODO: This should be a decorator
    def to_dict(self):
        return {'engine_endpoint_id': self.engine_endpoint_id, 'channel_name': self.channel_name,
                'latitude': self.latitude, 'longitude': self.longitude, 'elevation': self.elevation}
    
@dataclass(frozen=False)
class EndpointDescriptionField:
    engine_endpoint_description_id: int = None
    field1_name: str = None
    field2_name: str = None
    field3_name: str = None
    field4_name: str = None
    field5_name: str = None
    field6_name: str = None
    field7_name: str = None
    field8_name: str = None

    @property #TODO: This should be a decorator
    def to_dict(self):
        return {'engine_endpoint_description_id': self.engine_endpoint_description_id, 'field1_name': self.field1_name,
                'field2_name': self.field2_name, 'field3_name': self.field3_name, 'field4_name': self.field4_name,
                'field5_name': self.field5_name, 'field6_name': self.field6_name, 'field7_name': self.field7_name,
                'field8_name': self.field8_name}
