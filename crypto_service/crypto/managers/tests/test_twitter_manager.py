from unittest import TestCase
from unittest.mock import patch

from crypto.exceptions.api_exceptions import PlatformAPIError
from crypto.managers import TwitterManager

MODULE_PATH = "twitter_event_service.data_processor"


class TestTwitterManager(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "crypto_currency": {
                "name": "BTC",
                "start_date": "2020-04-12",
                "end_date": "2020-04-15",
            }
        }
        self.tweets = [
            "The whole point about bitcoin is to send it to whoever you want."
        ]
        self.twitter_manager = TwitterManager(
            input_data=self.input_data["crypto_currency"]
        )

    @patch(MODULE_PATH + ".TwitterDataProcessor.process_twitter_data_event")
    def test__extract_and_process_data_from_twitter(
        self, mock_process_twitter_data_event
    ):
        """Test ensures that the data from twitter is extracted successfully"""
        mock_process_twitter_data_event.return_value = self.tweets

        twitter_data = self.twitter_manager._extract_and_process_data_from_twitter()

        mock_process_twitter_data_event.assert_called_once_with(
            input_data=self.input_data["crypto_currency"]
        )

        self.assertEqual(twitter_data, mock_process_twitter_data_event.return_value)

    @patch(MODULE_PATH + ".TwitterDataProcessor.process_twitter_data_event")
    def test_do_call_twitter(self, mock_process_twitter_data_event):
        """Test ensures that a call to twitter is successfully made"""
        mock_process_twitter_data_event.return_value = self.tweets

        twitter_data = self.twitter_manager.do_call_twitter()

        mock_process_twitter_data_event.assert_called_once_with(
            input_data=self.input_data["crypto_currency"]
        )

        self.assertEqual(twitter_data, mock_process_twitter_data_event.return_value)

    @patch(MODULE_PATH + ".TwitterDataProcessor.process_twitter_data_event")
    def test_do_call_twitter_data_none(self, mock_process_twitter_data_event):
        """Test ensures that a custom exception is raised if there is a problem with the data
        from the twitter, if data is an empty list"""
        mock_process_twitter_data_event.return_value = []

        with self.assertRaises(PlatformAPIError):
            self.twitter_manager.do_call_twitter()

            mock_process_twitter_data_event.assert_called_once_with(
                input_data=self.input_data["crypto_currency"]
            )
