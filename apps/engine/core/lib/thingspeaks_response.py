import requests
from functools import lru_cache as memoized
from typing import Dict, List, Union, Iterator

from apps.engine.core.enums.thingspeaks import (
    ApiConstants,
    ApiParameters,
    ApiChannelResponse,
    ApiFeedResponse,
)

"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""


class ThingSpeaksRequestResponse:
    def __init__(
        self,
        channel_id: str,
        api_key: str = None,
        n_rows: int = None,
        interval: int = 30,
    ) -> None:
        self.parameters = ApiParameters(
            api_key=api_key, n_rows=n_rows, channel_id=channel_id, interval=interval
        )
        self._constants = ApiConstants

    @property
    @memoized(maxsize=1)
    def get_channel_response(self) -> Union[ApiChannelResponse, None]:
        if not self._get_thinkspeaks_response:
            return None
        response_from_channel = self._get_thinkspeaks_response.get(
            self._constants.channel_key
        )
        if not response_from_channel:
            return None
        return ApiChannelResponse(**response_from_channel)

    @property
    @memoized(maxsize=1)
    def get_feed_response(self) -> Union[Iterator[Dict], None]:
        if not self._get_thinkspeaks_response:
            return None
        response_from_feed = self._get_thinkspeaks_response.get(
            self._constants.feed_key
        )
        if response_from_feed is None:
            return None        
        for feed in response_from_feed:
            yield feed

    @property
    @memoized(maxsize=1)
    def _get_url(self) -> str:
        return f"{self._constants.url_base}/channels/{self.parameters.channel_id}/feeds.json?api_key=\
                {self.parameters.api_key}&results={self.parameters.n_rows}"

    @property
    @memoized(maxsize=1)
    def _get_thinkspeaks_response(self) -> Union[Dict, None]:
        json_response = None
        response = requests.get(self._get_url)
        if response.status_code == 200:
            json_response = response.json()
        return json_response
