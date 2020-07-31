# とりあえずtweetさせてみましょう
import settings
import json
import tweepy

API_KEY = settings.CK
API_SECRET_KEY = settings.CSK
ACCESS_TOKEN = settings.AT
ACCESS_TOKEN_SECRET = settings.ATS

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 好きな言葉をツイート
print("tweet > ")
api.update_status(input())