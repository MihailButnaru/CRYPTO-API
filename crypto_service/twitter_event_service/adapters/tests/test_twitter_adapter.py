from unittest import TestCase

from crypto.exceptions.api_exceptions import AuthenticationFailed
from twitter_event_service.adapters import init_twitter_connection


class TestTwitterConnection(TestCase):
    def test_twitter_connection_invalid(self):
        """Test ensures that the twitter connection is successfully"""

        with self.assertRaises(AuthenticationFailed):
            init_twitter_connection()
