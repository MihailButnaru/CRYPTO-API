from django.conf import settings

from twitter_event_service import init_twitter_connection
from twitter_event_service.helpers import get_tweets, CryptoEnum

__author__ = "Mihail Butnaru"
__copyright__ = "Copyright 2020, All rights reserved."


class TwitterDataProcessor:
    @staticmethod
    def _api_call_to_get_tweets(*, input_data: dict, crypto_name: str) -> list:
        api = init_twitter_connection()

        tweets = get_tweets(
            search_api=api.search,
            input_data=input_data,
            crypto_name=CryptoEnum(value=crypto_name).name.lower(),
            number_of_tweets=settings.NUMBER_OF_TWEETS,
        )

        return tweets

    def process_twitter_data_event(self, input_data: dict) -> list:
        return self._api_call_to_get_tweets(
            input_data=input_data, crypto_name=input_data["name"]
        )
