from sentiment_analysis import search_tweets_by_keyword, search_tweets_by_list


def get_tweet_count():
    tweet_count = input("Enter the number of tweets to retrieve (default: 50): ")

    if tweet_count.strip() == "":
        tweet_count = 50
    else:
        try:
            tweet_count = int(tweet_count)
        except ValueError:
            print("Invalid tweet count. Assuming default of 50.")
            tweet_count = 50

    return tweet_count


def main():
    print("Sentiment Analysis Program")
    print("==========================")
    print("1. Search by keyword")
    print("2. Search by Twitter list")
    choice = input("Enter your choice (1 or 2): ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Please enter a valid integer.")
        return

    if choice == 1:
        keyword = input("Enter the keyword to search: ")
        tweet_count = get_tweet_count()
        search_tweets_by_keyword(keyword, tweet_count)
    elif choice == 2:
        list_id = input("Enter the ID of the Twitter list: ")
        tweet_count = get_tweet_count()
        search_tweets_by_list(list_id, tweet_count)
    else:
        print("Invalid choice. Please try again.")
