from twitter_event_service import TwitterDataProcessor


class TwitterManager:
    def __init__(self, input_data: dict):
        self._data = input_data

    def _process_data_from_twitter(self):
        twitter_processor = TwitterDataProcessor()

        return twitter_processor.process_twitter_data_event(
            input_data=self._data
        )

    def do_call_twitter(self):
        """Calls the twitter processor from the twitter event service"""

        return self._process_data_from_twitter()
