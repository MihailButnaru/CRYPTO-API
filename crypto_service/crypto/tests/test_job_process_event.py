"""Tests to test the functionality of the JobProcessor"""
from unittest import TestCase
from unittest.mock import patch

from crypto.exceptions.api_exceptions import PlatformAPIError
from crypto.job_process_event import JobProcessor


class TestJobProcessor(TestCase):
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
        self.job_processor = JobProcessor()
        self.analyzed_data = {
            "sentence": "Did you get your stimulus check? If you dont need it for survival, here is a great option!",
            "polarity": 1.0,
            "subjectivity": 0.75,
        }

    def test__check_fields(self):
        fields = self.job_processor._check_fields(
            input_data=self.input_data["crypto_currency"]
        )

        self.assertTrue(fields)

    def test__check_fields_different(self):
        self.input_data["crypto_currency"]["test"] = 1.0

        fields = self.job_processor._check_fields(input_data=self.input_data)

        self.assertFalse(fields)

    @patch("crypto.managers.twitter_manager.TwitterManager.do_call_twitter")
    def test__get_data_from_twitter(self, mock_do_call_twitter):
        mock_do_call_twitter.return_value = self.tweets

        twitter_data = self.job_processor._get_data_from_twitter(
            input_data=self.input_data
        )

        mock_do_call_twitter.assert_called_once_with()

        self.assertEqual(twitter_data, mock_do_call_twitter.return_value)

    @patch(
        "nlp_event_service.text_processing_runner.ProcessEventTextRunner.do_call_to_process_sentences"
    )
    def test__analyse_data(self, mock_do_call_to_process_sentences):
        mock_do_call_to_process_sentences.return_value = self.analyzed_data

        data = self.job_processor._analyse_data(twitter_data=self.tweets)

        mock_do_call_to_process_sentences.assert_called_once_with(data=self.tweets)

        self.assertEqual(data, mock_do_call_to_process_sentences.return_value)

    @patch(
        "nlp_event_service.text_processing_runner.ProcessEventTextRunner.do_call_to_process_sentences"
    )
    @patch("crypto.managers.twitter_manager.TwitterManager.do_call_twitter")
    def test_start_job_process(
        self, mock_do_call_twitter, mock_do_call_to_process_sentences
    ):
        mock_do_call_twitter.return_value = self.tweets
        mock_do_call_to_process_sentences.return_value = self.analyzed_data

        data = self.job_processor.start_job_process(
            input_data=self.input_data["crypto_currency"]
        )

        mock_do_call_twitter.assert_called_once_with()

        mock_do_call_to_process_sentences.assert_called_once_with(data=self.tweets)

        self.assertEqual(data, mock_do_call_to_process_sentences.return_value)

    def test_start_job_process_error(self):
        with self.assertRaises(PlatformAPIError):
            self.job_processor.start_job_process(input_data=self.input_data)
