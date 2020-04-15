from crypto.exceptions.api_exceptions import PlatformAPIError
from crypto.managers import TwitterManager
from nlp_event_service import ProcessEventTextRunner

__author__ = "Mihail Butnaru"
__copyright__ = "Copyright 2020, All rights reserved."


class JobProcessor:
    @staticmethod
    def _check_fields(input_data: dict) -> bool:
        data = {"name", "start_date", "end_date"}
        return any([key in set(input_data) for key in data])

    @staticmethod
    def _get_data_from_twitter(input_data: dict) -> list:
        """Gets the twitter data by calling the Twitter API"""
        twitter_manager = TwitterManager(input_data=input_data)

        return twitter_manager.do_call_twitter()

    @staticmethod
    def _analyse_data(twitter_data: list) -> list:
        event_runner = ProcessEventTextRunner()
        analysed_data = event_runner.do_call_to_process_sentences(data=twitter_data)
        return analysed_data

    @classmethod
    def start_job_process(cls, input_data: dict) -> list:
        """ Starts the process of getting the data from the twitter, cleans
        the noise data and it determines the sentiment analysis of the tweets.
        """
        if not cls._check_fields(input_data=input_data):
            raise PlatformAPIError(
                detail="Service temporarily has an error, contact the administrator"
            )

        twitter_data = cls._get_data_from_twitter(input_data=input_data)

        analyzed_data = cls._analyse_data(twitter_data=twitter_data)

        return analyzed_data
