# TweetBot
TestMessage : Hello World

TestMessage : ishiharadesu

TestMessage2 : Kon-nitiwa!
TestMessage3 : gitインストール完了

## AWS Lambda への関数の追加方法
1. スクリプトについて
    - 動かしたいメインの部分を関数として（きちんとdef function(event, context):を用いて名付けたうえで）スクリプトを書く．
1. AWSへのアップロードについて
    - 使用する外部ライブラリ（tweepyなど）も一緒にAWS上にアップロードする必要があるため，適当なディレクトリにインストールする．
    - 外部ライブラリと自前のスクリプトを一つのzipにまとめ，AWSにアップロードする．
1. AWS上での設定について
    - zipファイルのアップロード後，実行したいスクリプトとメインの関数を「基本設定-ハンドラ」で設定する．
    - token等を環境変数に追加する
    - 定期的に関数を実行させるため，トリガーのEventBridge(CloudWatch Events)を設定する．
