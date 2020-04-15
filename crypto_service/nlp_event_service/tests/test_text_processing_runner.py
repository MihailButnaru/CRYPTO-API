from unittest import TestCase

from nlp_event_service import ProcessEventTextRunner


class TestProcessEventTextRunner(TestCase):
    def setUp(self) -> None:
        self.sentences = [
            "Did you get your stimulus check? If you dont need it for survival, here is a great option!",
            ": 🥳$50 ONE PERSON GETS 074 🤑 🧜‍️Rules: Like &amp; Retweet Follow …",
        ]
        self.process_event_text_runner = ProcessEventTextRunner()

    def test__remove_noise(self):
        """Test ensures that it removes the noise from the dataset"""
        cleaned_data = self.process_event_text_runner._remove_noise(
            sentences=self.sentences
        )

        expected_data = [
            "Did you get your stimulus check? If you dont need it for survival, here is a great option!",
            ": 🥳$50 ONE PERSON GETS 074 money-mouth_face 🧜‍️Rules: Like &amp; Retweet Follow …",
        ]

        self.assertEqual(cleaned_data, expected_data)

    def test__process_the_sentiment_analysis(self):
        """Test ensures that it process the sentiment analysis"""
        analysis = self.process_event_text_runner._process_the_sentiment_analysis(
            data=self.sentences
        )

        expected_payload = [
            {
                "sentence": "Did you get your stimulus check? If you dont need it for survival, here is a great option!",
                "polarity": 1.0,
                "subjectivity": 0.75,
            },
            {
                "sentence": ": 🥳$50 ONE PERSON GETS 074 🤑 🧜\u200d️Rules: Like &amp; Retweet Follow …",
                "polarity": 0.0,
                "subjectivity": 0.0,
            },
        ]

        self.assertEqual(analysis, expected_payload)

    def test_do_call_to_process_sentences(self):
        """Test ensures that it process the sentences to analyse the sentiment
        analysis."""

        data = self.process_event_text_runner.do_call_to_process_sentences(
            data=self.sentences
        )

        expected_payload = [
            {
                "sentence": "Did you get your stimulus check? If you dont need it for survival, here is a great option!",
                "polarity": 1.0,
                "subjectivity": 0.75,
            },
            {
                "sentence": ": 🥳$50 ONE PERSON GETS 074 money-mouth_face 🧜\u200d️Rules: Like &amp; Retweet Follow …",
                "polarity": 0.0,
                "subjectivity": 0.0,
            },
        ]

        self.assertEqual(data, expected_payload)
