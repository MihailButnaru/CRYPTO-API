# Copyright 2020
# All rights reserved. Mihail Butnaru
import logging

import tweepy
from django.conf import settings
from tweepy import TweepError

from crypto.exceptions.api_exceptions import AuthenticationFailed

_logger = logging.getLogger(__name__)


def init_twitter_connection() -> tweepy.API:
    """Initialize the twitter connection in order to get
    access to the twitter data. """
    auth = tweepy.OAuthHandler(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
    )
    auth.set_access_token(
        key=settings.TWITTER_ACCESS_TOKEN, secret=settings.TWITTER_ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except TweepError:
        raise AuthenticationFailed(detail="Invalid credentials")
    return api
