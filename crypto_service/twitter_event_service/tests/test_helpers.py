from datetime import date
from unittest import TestCase

from twitter_event_service.helpers import _get_tweet_between_end_start_date


class TestHelpers(TestCase):
    def setUp(self) -> None:
        self.tweet_created_date = date(2020, 4, 14)
        self.input_data = {
            "crypto_currency": {
                "name": "BTC",
                "start_date": date(2020, 4, 13),
                "end_date": date(2020, 4, 15),
            }
        }
        self.tweets = [
            "The whole point about bitcoin is to send it to whoever you want."
        ]

    def test__get_tweet_between_end_and_start_date_true(self):
        """Test ensures that a validation between the data is successfully
        executed"""

        date_bool = _get_tweet_between_end_start_date(
            tweet_created_date=self.tweet_created_date,
            input_data=self.input_data["crypto_currency"],
        )

        self.assertTrue(date_bool)

    def test__get_tweet_between_end_and_start_date_false(self):
        """Test ensures that a validation between the data is successfully
        executed"""
        self.tweet_created_date = date(2020, 4, 20)

        date_bool = _get_tweet_between_end_start_date(
            tweet_created_date=self.tweet_created_date,
            input_data=self.input_data["crypto_currency"],
        )

        self.assertFalse(date_bool)
