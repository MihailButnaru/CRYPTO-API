from google_event_service import GoogleDataProcessor


class GoogleManager:

    @staticmethod
    def _prepare_data_to_analyse(tweets: list):
        google_processor = GoogleDataProcessor()
        return google_processor.process_google_data_event(
            tweets=tweets
        )

    @classmethod
    def do_call_google(cls, tweets: list):
        """Calls the google processor to analyse the tweets
        from the Twitter"""
        # if not tweets:
        #     raise ValueError("Empty list")
        return cls._prepare_data_to_analyse(tweets=tweets)
