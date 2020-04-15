from google_event_service.adapters.google_adapter import init_google_connection
from google_event_service.helpers import process_text_to_analyze


class GoogleDataProcessor:

    @staticmethod
    def _api_call_to_process_sentiments_of_tweets(tweets: list):
        api_client = init_google_connection()
        for document in process_text_to_analyze(['I am a good boy', 'I am a bad boy']):
            sentiment = api_client.analyze_sentiment(document=document).document_sentiment
            print(sentiment)

    def process_google_data_event(self, tweets: list):
        return self._api_call_to_process_sentiments_of_tweets(tweets=tweets)
