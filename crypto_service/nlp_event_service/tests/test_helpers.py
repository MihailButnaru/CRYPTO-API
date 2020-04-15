from unittest import TestCase

from nlp_event_service.helpers import convert_emojis


class TestHelpers(TestCase):
    def setUp(self) -> None:
        self.text = "I love python 👨"

    def test_convert_emojis(self):
        """Test ensures that you can convert the emojis successfully"""
        text_emoji = convert_emojis(text=self.text)

        self.assertEqual(text_emoji, "I love python man")
