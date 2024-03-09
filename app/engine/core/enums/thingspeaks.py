from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ApiConstants:
    url_base: str = 'https://api.thingspeak.com'
    channel_key: str = 'channel'
    feed_key: str = 'feeds'

@dataclass
class ApiParameters:
    api_key: Optional[str] = None #None if it is a public channel
    n_rows: Optional[int] = None
    channel_id: str
    interval: int

@dataclass
class ApiChannelResponse:
    id: str
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    created_at: str
    updated_at: str
    elevation: Optional[float] = None
    last_entry_id: int    
    field1: Optional[str] = None
    field2: Optional[str] = None
    field3: Optional[str] = None
    field4: Optional[str] = None
    field5: Optional[str] = None
    field6: Optional[str] = None
    field7: Optional[str] = None
    field8: Optional[str] = None

@dataclass
class ApiFeedResponse:
    created_at: str
    entry_id: int
    field1: Optional[str] = None
    field2: Optional[str] = None
    field3: Optional[str] = None
    field4: Optional[str] = None
    field5: Optional[str] = None
    field6: Optional[str] = None
    field7: Optional[str] = None
    field8: Optional[str] = None 
