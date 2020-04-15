from typing import Union

from crypto.exceptions.api_exceptions import PlatformAPIError
from twitter_event_service import TwitterDataProcessor


class TwitterManager:
    def __init__(self, input_data: dict):
        self._data = input_data

    def _extract_process_data_from_twitter(self) -> list:
        """Extracts the data from the twitter API."""
        twitter_processor = TwitterDataProcessor()

        twitter_data = twitter_processor.process_twitter_data_event(
            input_data=self._data
        )
        return twitter_data

    def do_call_twitter(self) -> Union[list, PlatformAPIError]:
        """Call to the twitter to process and to extract the data from the
        twitter API. [twitter_event_service used]
        """
        twitter_data = self._extract_process_data_from_twitter()

        if not twitter_data:
            return PlatformAPIError(
                detail="There was a problem with extract data from the twitter"
            )

        return twitter_data
