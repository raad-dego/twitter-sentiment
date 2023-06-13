from config import authenticate_api
import tweepy


def test_twitter_api():
    try:
        api = authenticate_api()
        user = api.verify_credentials()
        print(f"Connected to Twitter API as: {user.screen_name}")
    except tweepy.error.TweepError as e:
        print(f"Failed to connect to Twitter API. Error message: {str(e)}")


# Test the Twitter API connection
test_twitter_api()
