import tweepy as tw

__jaccard_threshold__ = .25
def jaccard_similariy_index(first, second):
    """
    Returns the jaccard similarity between two strings
    :param first: first string we are comparing
    :param second: second string we are comparing
    :return: how similar the two strings are
    """

    # First, split the sentences into words
    tokenize_first = set(first.lower().split())
    tokenize_second = set(second.lower().split())

    # Then, find the ratio between their intersection and their total length
    intersection = tokenize_first.intersection(tokenize_second)
    return float(len(intersection)) / (len(tokenize_first) + len(tokenize_second) - len(intersection))

__number_of_tweets__ = 5

def scrape_tweets(handle, number_of_tweets):
    """
    Function to scrape tweets based on a user handle
    :param handle: The user's twitter handle
    :param number_of_tweets: The number of tweets we want to get
    :return: (number_of_tweets) tweets from a user
    """
    consumer_key = "bDTIoK0pn0gX7oniVhnI1ewnU"
    consumer_secret = "KaHGOEkkUculbGAWOJ8KDSRxRH1GU4ZpLLuRRrlQFoasDa0msm"
    access_token_key = "2386644165-wA8wZ6jGFv4OB9Enz9F53ynSrydDXADPy0QAL0X"
    access_token_secret = "SXlOrRpfGJESQvWODV1fMZpzwLn9Pu7BR4vJnQF86dKLz"

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    tweets = list()
    try:
        for tweet in api.home_timeline(id=handle, count=number_of_tweets):
            timestamp = tweet.created_at
            id = tweet.id
            text = tweet.text
            media = tweet.entities.get('media', [])
            if (len(media) > 0):
                media = media[0]['media_url']
            tweets.append({
                "timestamp": timestamp,
                "id": id,
                "text": text,
                "media": media
            })

    except BaseException as e:
        print("failed for some reason: {}".format(e))

    return tweets


def check_if_tweet_in_user(tweet_to_check, handle):
    """
    Checks if a user's recent tweets contains a particular tweet
    :param tweet_to_check: text of the tweet that we're checking
    :param handle: user's handle
    :return: whether or not the user's recent tweets contains that particular text
    """
    user_tweets = scrape_tweets(handle, __number_of_tweets__)

    for tweet in user_tweets:
        if jaccard_similariy_index(tweet_to_check, tweet['text']) > __jaccard_threshold__:
            return True
    return False

def verify_twitter(user, poke):
    if (check_if_tweet_in_user(poke['data']['body'], user['user_credentials']['twitter_uname'])):
        return poke['pts']
    return None