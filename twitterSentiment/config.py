import tweepy
from dotenv import load_dotenv
import os

load_dotenv()


def authenticate_api():
    oauth_consumer_key = os.getenv("CONSUMER_KEY")
    oauth_consumer_secret = os.getenv("CONSUMER_SECRET")
    oauth_token = os.getenv("ACCESS_TOKEN")
    oauth_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(oauth_consumer_key, oauth_consumer_secret)
    auth.set_access_token(oauth_token, oauth_token_secret)

    api = tweepy.API(auth)
    return api
