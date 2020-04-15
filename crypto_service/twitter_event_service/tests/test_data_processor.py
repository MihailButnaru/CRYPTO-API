from unittest import TestCase
from unittest.mock import patch

from twitter_event_service import TwitterDataProcessor

MODULE_PATH = "twitter_event_service.data_processor"


class TestTwitterDataProcessor(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "crypto_currency": {
                "name": "BTC",
                "start_date": "2020-04-14",
                "end_date": "2020-04-15",
            }
        }
        self.tweets = [
            "The whole point about bitcoin is to send it to whoever you want."
        ]
        self.number_of_tweets = 500
        self.crypto_name = "bitcoin"
        self.twitter_data_processor = TwitterDataProcessor()

    @patch("twitter_event_service.data_processor.get_tweets")
    @patch("twitter_event_service.data_processor.init_twitter_connection")
    def test__api_call_to_get_tweets(
        self, mock_init_twitter_connection, mock_get_tweets
    ):
        """Test ensures that the api call get the tweets"""
        mock_init_twitter_connection.search.return_value = True
        mock_get_tweets.return_value = self.tweets

        tweets = self.twitter_data_processor._api_call_to_get_tweets(
            input_data=self.input_data,
            crypto_name=self.input_data["crypto_currency"]["name"],
        )

        mock_init_twitter_connection.assert_called_once_with()

        mock_get_tweets.assert_called_once_with(
            search_api=mock_init_twitter_connection().search,
            input_data=self.input_data,
            crypto_name=self.crypto_name,
            number_of_tweets=self.number_of_tweets,
        )

        self.assertTrue(tweets, mock_get_tweets.return_value)

    @patch(MODULE_PATH + ".get_tweets")
    @patch(MODULE_PATH + ".init_twitter_connection")
    def test_process_twitter_data_event(
        self, mock_init_twitter_connection, mock_get_tweets
    ):
        """Test ensures that the data from twitter is processed and extracted"""
        mock_init_twitter_connection.search.return_value = True
        mock_get_tweets.return_value = self.tweets

        tweets = self.twitter_data_processor.process_twitter_data_event(
            input_data=self.input_data["crypto_currency"]
        )

        mock_init_twitter_connection.assert_called_once_with()

        mock_get_tweets.assert_called_once_with(
            search_api=mock_init_twitter_connection().search,
            input_data=self.input_data["crypto_currency"],
            crypto_name=self.crypto_name,
            number_of_tweets=self.number_of_tweets,
        )

        self.assertTrue(tweets, mock_get_tweets.return_value)
