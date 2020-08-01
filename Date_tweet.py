import tweepy
import settings
import datetime

# KEYの読みこみ
API_KEY = settings.CK
API_SECRET_KEY = settings.CSK
ACCESS_TOKEN = settings.AT
ACCESS_TOKEN_SECRET = settings.ATS

#Lambdaが実行すべき部分を認識するために，lambda_handler()としなければならない
def lambda_handler(event, context):
    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #現在時刻の発言
    now = datetime.datetime.now()
    dt_now = now.strftime('%Y/%m/%d %H:%M:%S')
    api.update_status("今は "+dt_now)

lambda_handler(None, None)