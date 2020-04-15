import re

from textblob import TextBlob

from nlp_event_service.helpers import convert_emojis


class ProcessEventTextRunner:
    @staticmethod
    def _remove_noise(sentences: list) -> list:
        """Removes the noise from the datasets, the function
        first searches for a substring that matches a URL, followed
        by letters, numbers or special characters and it replaces with
        an empty string, it also removes the mention tag @ from the sentence
        """
        cleaned_data = []

        for sentence in sentences:
            sentence = re.sub(
                "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|"
                "(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                "",
                sentence,
            )
            sentence = re.sub("(@[A-Za-z0-9_]+)", "", sentence)
            sentence = convert_emojis(text=sentence)

            cleaned_data.append(sentence)
        return cleaned_data

    @staticmethod
    def _process_the_sentiment_analysis(data: list) -> list:
        """Process the sentiment analysis from the cleaned data"""
        sentiment_analysis = []

        for sentence in data:
            text_analysis = TextBlob(sentence)
            sentiment_analysis.append(
                {
                    "sentence": sentence,
                    "polarity": text_analysis.sentiment.polarity,
                    "subjectivity": text_analysis.sentiment.subjectivity,
                }
            )

        return sentiment_analysis

    def do_call_to_process_sentences(self, data: list) -> list:
        """ Calls the sentiment analysis processor to analyse and process
        the sentiment analysis of the sentences (tweets).
        Returns the correct result of analysis.
        """
        cleaned_data = self._remove_noise(sentences=data)

        data = self._process_the_sentiment_analysis(data=cleaned_data)

        return data
