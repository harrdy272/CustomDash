import tweepy
import pandas as pd

# input your credentials here
consumer_key = 'trV2J2wuMIrMUHmXH0cxgCZN0'
consumer_secret = 'jqAn2KwClnG1zIEgcaKQUY4vBUV6MHZQ7M2Zt7VdQ7oV0IMiJo'
access_token = '2463420950-gxvBE17pLVW6cBFc6Y8QAflWXCprwAM68N97nk5'
access_token_secret = 'xedRAqzfjjF0oBeUW16Spbw0EBIhZbgq39OU9VhAbzj2R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets_df = pd.DataFrame(columns=['timestamp', 'tweet'])

timestamp = []
tweets = []

for tweet in tweepy.Cursor(api.search, q="#Vodafone", tweet_mode='extended', count=100, lang="en", since="2017-04-03").items():
    print(tweet.created_at, tweet.full_text)
    timestamp.append(tweet.created_at)
    tweets.append(tweet.full_text)

for tweet in tweepy.Cursor(api.search, q="#vodafoneidea", tweet_mode='extended', count=100, lang="en", since="2017-04-03").items():
    print(tweet.created_at, tweet.full_text)
    timestamp.append(tweet.created_at)
    tweets.append(tweet.full_text)

tweets_df['tweet'] = tweets
tweets_df['timestamp'] = timestamp

tweets_df.to_csv("../appdata/vodafoneidea_tweets.csv", index=False)
