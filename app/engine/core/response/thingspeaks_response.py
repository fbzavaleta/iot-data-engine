import requests
from functools import lru_cache as memoized
from typing import Dict, List, Union, Iterator

from app.engine.core.enums.thingspeaks import (
    ApiConstants, ApiParameters, ApiChannelResponse, ApiFeedResponse
) 


class ThingSpeaksRequestResponse:
    def __init__(self, channel_id: str, api_key: str=None, n_rows: int=None
                 , interval: int=30) -> None:
        self.parameters = ApiParameters(api_key=api_key, n_rows=n_rows, channel_id=channel_id
                                        , interval=interval)
        self._constants = ApiConstants

    @property
    @memoized(maxsize=1)
    def get_channel_response(self) -> Iterator[ApiChannelResponse]:
        if not self._get_thinkspeaks_response:
            raise ValueError("No response from ThingSpeaks")
        response_from_channel = self._get_thinkspeaks_response.get(self._constants.channel_key)
        for feed in response_from_channel:
            yield ApiChannelResponse(**feed)

    @property
    @memoized(maxsize=1)
    def get_feed_response(self) -> Union[List, None]:
        feed_response = None
        if self._get_thinkspeaks_response:
            response_from_feed = self._get_thinkspeaks_response.get(self._constants.feed_key)
            feed_response = ApiFeedResponse(**response_from_feed)
        return feed_response

    @property
    @memoized(maxsize=1)
    def _get_url(self) -> str:
        return f"{self._constants.url_base}/channels/{self.parameters.channel_id}/feeds.json?api_key=\
                {self.parameters.api_key}&results={self.parameters.n_rows}"
    
    @property
    @memoized(maxsize=1)
    def _get_thinkspeaks_response(self) -> Union[Dict, None]:
        json_response = None
        response =  requests.get(self._get_url)
        if response.status_code == 200:
            json_response = response.json()
        return json_response
