'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Twitter API -
Takes in twitter credentials & message, formats the message & posts it
Leverages on Tweepy package to connect to Twitter API endpoint
'''

import tweepy
import os
ckey = os.environ.get('TWITTER_CKEY')
csecret = os.environ.get('TWITTER_CSECRET')
atoken = os.environ.get('TWITTER_ATOKEN')
asecret = os.environ.get('TWITTER_ASECRET')
#Get API keys from env
# from configparser import ConfigParser
# config = ConfigParser()
# config.read('config.ini')
# ckey = config.get('twitter', 'ckey')
# csecret = config.get('twitter', 'csecret')
# atoken = config.get('twitter', 'atoken')
# asecret = config.get('twitter', 'asecret')

## TODO: IMPLEMENT ERROR HANDLING IF EXCESS 140 CHAR

def main(data):
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    print('Twitter Authentication Complete')
    api = tweepy.API(auth)
    post(api, data)

def post(api, data):
    api.update_status(data)
    print(data)
    print("Twitter Post Successful")

