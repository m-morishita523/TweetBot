# とりあえずtweetさせてみましょう
import settings
import json
from requests_oauthlib import OAuth1Session

API_KEY = settings.CK
API_SECRET_KEY = settings.CSK
ACCESS_TOKEN = settings.AT
ACCESS_TOKEN_SECRET = settings.ATS
twitter = OAuth1Session(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN)  #OAuth認証
print(twitter)