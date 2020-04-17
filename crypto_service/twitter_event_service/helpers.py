from datetime import date
from enum import Enum

import preprocessor as tweet_data
import tweepy
from tweepy.binder import bind_api

__author__ = "Mihail Butnaru"
__copyright__ = "Copyright 2020, All rights reserved."


class CryptoEnum(Enum):
    BITCOIN = "BTC"
    ETHEREUM = "ETH"
    RIPPLE = "XRP"


def _get_tweet_between_end_start_date(
        *, tweet_created_date: date, input_data: dict
) -> bool:
    return (
            tweet_created_date <= input_data["end_date"]
            and tweet_created_date >= input_data["start_date"]
    )


def get_tweets(
        *, search_api: bind_api, input_data: dict, crypto_name: str, number_of_tweets: int
) -> list:
    tweets = []
    for tweet in tweepy.Cursor(
            search_api, q=f"{crypto_name}", lang="en", result_type="recent"
    ).items(number_of_tweets):
        if _get_tweet_between_end_start_date(
                tweet_created_date=tweet.created_at.date(), input_data=input_data
        ):
            tweets.append(tweet_data.clean(tweet.text))
    return tweets
