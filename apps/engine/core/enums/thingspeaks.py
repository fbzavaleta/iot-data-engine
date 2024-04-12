from dataclasses import dataclass
from typing import Optional

"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""


@dataclass(frozen=True)
class ApiConstants:
    url_base: str = "https://api.thingspeak.com"
    channel_key: str = "channel"
    feed_key: str = "feeds"


@dataclass(frozen=False)
class ApiParameters:
    channel_id: str = None
    api_key: Optional[str] = None
    interval: int = None
    n_rows: Optional[int] = None
    endpoint_id: Optional[id] = None

    def __init__(
        self,
        channel_id: Optional[str] = None,
        api_key: Optional[str] = None,
        interval: Optional[int] = None,
        n_rows: Optional[int] = None,
        endpoint_id: Optional[int] = None,
        **kwargs
    ) -> None:
        self.channel_id = channel_id
        self.api_key = api_key
        self.interval = interval
        self.n_rows = n_rows
        self.endpoint_id = endpoint_id


@dataclass(frozen=False)
class ApiChannelResponse:
    id: str
    name: str
    latitude: float
    longitude: float
    created_at: str
    updated_at: str
    last_entry_id: int
    description: Optional[str] = None
    elevation: Optional[float] = None
    field1: Optional[str] = None
    field2: Optional[str] = None
    field3: Optional[str] = None
    field4: Optional[str] = None
    field5: Optional[str] = None
    field6: Optional[str] = None
    field7: Optional[str] = None
    field8: Optional[str] = None


@dataclass(frozen=False)
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
