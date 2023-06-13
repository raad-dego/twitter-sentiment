from config import authenticate_api
from textblob import TextBlob


def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    sentiment = analysis.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity
    emotions = analysis.emotions

    return polarity, subjectivity, emotions


def perform_sentiment_analysis(tweets):
    sentiment_distribution = {"positive": 0, "negative": 0, "neutral": 0}
    total_polarity = 0
    total_subjectivity = 0

    for tweet in tweets:
        print(tweet.text)
        polarity, subjectivity, emotions = analyze_sentiment(tweet.text)
        print("Sentiment Polarity:", polarity)
        print("Subjectivity:", subjectivity)
        print("Emotions:", emotions)
        print('------')

        # Update sentiment distribution
        if polarity > 0:
            sentiment_distribution["positive"] += 1
        elif polarity < 0:
            sentiment_distribution["negative"] += 1
        else:
            sentiment_distribution["neutral"] += 1

        # Calculate total polarity and subjectivity
        total_polarity += polarity
        total_subjectivity += subjectivity

    # Calculate average polarity and subjectivity
    average_polarity = total_polarity / len(tweets)
    average_subjectivity = total_subjectivity / len(tweets)

    print("Sentiment Distribution:", sentiment_distribution)
    print("Average Polarity:", average_polarity)
    print("Average Subjectivity:", average_subjectivity)


def search_tweets_by_keyword(keyword, tweet_count=50):
    api = authenticate_api()
    tweets = api.search(q=keyword, count=tweet_count)
    perform_sentiment_analysis(tweets)


def search_tweets_by_list(list_id, tweet_count=50):
    api = authenticate_api()
    tweets = api.list_timeline(list_id=list_id, count=tweet_count)
    perform_sentiment_analysis(tweets)
