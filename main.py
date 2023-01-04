import tweepy
from time import sleep
import os
import random

consumerKey = ''
consumerSecret = ''
accessToken = ''
accessTokenSecret = ''

auth = tweepy.OAuth1UserHandler(
       consumerKey,
       consumerSecret,
       accessToken,
       accessTokenSecret
    )

api = tweepy.API(auth)

def main():
    while True:
        media = api.media_upload(filename=f"images/{pic()}")
        api.update_status("", media_ids = [media.media_id_string])
        sleep(60)

def pic():
    i = os.listdir('images')
    r = random.choice(i)
    return r

main()