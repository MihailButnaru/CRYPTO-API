from datetime import date
from enum import Enum

import preprocessor as tweet_data
import tweepy


class CryptoEnum(Enum):
    BITCOIN = "BTC"


def _get_tweet_between_end_start_date(*, tweet_created_date: date, input_data: dict) -> bool:
    if tweet_created_date <= input_data["end_date"] and tweet_created_date >= input_data["start_date"]:
        return True
    return False


def get_tweets(*, connector, input_data: dict, crypto_name: str, number_of_tweets: int):
    tweets = []
    for tweet in tweepy.Cursor(connector,
                               q=f"{crypto_name}",
                               lang="en",
                               result_type="recent").items(number_of_tweets):
        if _get_tweet_between_end_start_date(tweet_created_date=tweet.created_at.date(), input_data=input_data):
            tweets.append(tweet_data.clean(tweet.text))
    return tweets
