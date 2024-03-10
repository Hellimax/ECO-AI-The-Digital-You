import twitter_scrapper
import ner
import llama2_model

def get_tweets(url):
    tweets = twitter_scrapper.get_tweets(url)
    tweet_raw_text = ""
    for tweet in tweets:
        tweet_raw_text = tweet_raw_text+"'"+tweet+"'"+"\n\n"
    
    return tweet_raw_text

tweet_raw_text = get_tweets("https://twitter.com/RishiSunak")

#ner.get_ners(tweet_raw_text)

llama2_model.generate_personlised_tweet(tweet_raw_text)