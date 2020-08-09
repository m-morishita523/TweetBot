import settings
import tweepy

# KEYの読みこみ
API_KEY = settings.CK
API_SECRET_KEY = settings.CSK
ACCESS_TOKEN = settings.AT
ACCESS_TOKEN_SECRET = settings.ATS

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#1ツイートずつループ
for status in api.home_timeline(count=5):
    #見映えのため区切る
    print('-------------------------------------------')
    #ユーザ名表示
    print('name:' + status.user.name)
    #内容表示
    print(status.text)