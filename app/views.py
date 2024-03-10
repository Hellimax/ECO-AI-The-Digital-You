from django.shortcuts import render
from django.http import JsonResponse
import app.twitter_scrapper as twitter_scrapper
import app.ner as ner
import app.llama2_model as llama2_model


def get_tweets(url):
    tweets = twitter_scrapper.get_tweets(url)
    tweet_raw_text = ""
    for tweet in tweets:
        tweet_raw_text = tweet_raw_text+"'"+tweet+"'"+"\n\n"
    
    return tweet_raw_text

# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def get_interests(request):
    url = request.GET["url"]
    global all_tweets
    all_tweets = get_tweets(url)
    ners = ner.get_ners(all_tweets)
    return JsonResponse({
        "data": ners
    })


def generate_tweet(request):
    interest_description = request.GET['interest_input']
    generated_tweet = llama2_model.generate_personlised_tweet(all_tweets,interest_description)
    return JsonResponse({
        "data": generated_tweet
    })