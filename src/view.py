#codeing: utf-8

from flask import Flask, render_template

#Flaskをインスタンス化
app = Flask(__name__)

#___view側の設定＿＿＿
#ルートディレクトリにアクセスした場合の挙動
@app.route('/')
#def以下がアクセス後の操作
def index():
    #return 'Hello World だぞ!'
    return render_template("index.html")

#エントリーポイントao

if __name__=='__main__':
    app.run()

