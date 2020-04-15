from crypto.managers import TwitterManager
from nlp_event_service import ProcessEventTextRunner
from crypto.exceptions.api_exceptions import PlatformAPIError


class JobProcessor:
    @staticmethod
    def _check_data(input_data: dict) -> bool:
        data = {"name", "start_date", "end_date"}
        return any([key in data for key in set(input_data)])

    @staticmethod
    def _get_twitter_data(input_data: dict) -> list:
        """Gets the twitter data by calling the Twitter API"""
        twitter_manager = TwitterManager(input_data=input_data)

        return twitter_manager.do_call_twitter()

    @staticmethod
    def _analyze_data(twitter_data: list) -> list:
        event_runner = ProcessEventTextRunner()
        analyzed_data = event_runner.do_call_to_process_sentences(data=twitter_data)
        return analyzed_data

    @classmethod
    def start_job_process(cls, input_data: dict) -> list:
        """ Starts the process of getting the data from the twitter, cleans
        the noise data and it determines the sentiment analysis of the tweets.
        """
        if not cls._check_data(input_data=input_data):
            raise PlatformAPIError(
                detail="Service temporarily has an error, contact the administrator"
            )

        twitter_data = cls._get_twitter_data(input_data=input_data)

        analyzed_data = cls._analyze_data(twitter_data=twitter_data)

        return analyzed_data
