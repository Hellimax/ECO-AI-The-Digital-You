from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_tweets(twitter_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    #service = Service('./chromedriver.exe')  # Path to your chromedriver executable

    tweet_collection = []
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(twitter_url)
    increment = 0.1
    while len(tweet_collection)<=10:
        time.sleep(3)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        inner_list = soup.find_all("div",{'data-testid':'cellInnerDiv'})
        for i in range(len(inner_list)):
            inner_cell = inner_list[i].find('div',{'data-testid':'tweetText'})
            if inner_cell != None:
                tweet_segments = inner_cell.find_all()
                complete_tweet = [tweet_segments[0].text]

                for i in range(1,len(tweet_segments)):
                    if tweet_segments[i].text != tweet_segments[i-1].text:
                        complete_tweet.append(tweet_segments[i].text)

                complete_tweet = ''.join(complete_tweet)
                #print(complete_tweet)
                if all(complete_tweet != s for s in tweet_collection):
                    tweet_collection.append(complete_tweet)
        page_height = driver.execute_script("return document.body.scrollHeight")
        scroll_distance = page_height * increment
        driver.execute_script("window.scrollTo(0, arguments[0]);", scroll_distance)
        increment = increment+0.1

    driver.quit()
    return(tweet_collection)

if __name__=="__main__":
    tweet_collection = get_tweets("https://twitter.com/KevinHart4real")
    print(tweet_collection)