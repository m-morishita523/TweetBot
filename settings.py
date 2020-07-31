# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("API_KEY") # 環境変数の値をAPに代入
CS = os.environ.get("API_SECRET_KEY")
AT = os.environ.get("ACCESS_TOKEN")
ATS = os.environ.get("ACCESS_TOKEN_SECRET")