import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup as bs4
import ssl
import random

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    ssl._create_default_https_context = ssl._create_unverified_context

    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""
    with urlopen("https://nabe-mania.com/") as res:
        html = res.read().decode("utf-8")
    #レスポンスのHTMLから　BeautifulSoup オブジェクトを作る    
    soup = bs4 (html,"html.parser")

    #a　タグの要素を取得する
    titles = soup.select("h2")
    links = [url.get('href') for url in soup.select('h2')]
    #item = soup.find_all("item") でもOK

     # 3. 記事一覧を取得する
    titles = [t.string for t in titles] #←これ何？

    # 4. ランダムに1件取得する
    # titleの要素数内でランダムで整数を生成。その番号の要素を取り出す
    i = random.randint(0,len(titles)-1)
    titles = titles[i]
    links = links[i]

    # 5. 以下の形式で返却する.
    return json.dumps({
        "content" : titles,
        "link" : links
    })

    if __name__ == " __main__ " :
        app.run(debug=True, port=5000)

    """
    #itemをシャッフルする
    shuffle(tags)
    #items　の一つ目を取得する
    tag = tags[0]
    print(tag)
    return json.dumps({
        "content" : tag.find("link").string,
        #"link" : item.find("link").string
        "link" : tag.get('rdf:about')
    })
    """

    """


    
    
        **** ここを実装します（基礎課題） ****
        1. はてブのホットエントリーページのHTMLを取得する
        2. BeautifulSoupでHTMLを読み込む
        3. 記事一覧を取得する
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """

    # ダミー
    return json.dumps({
        "content" : "記事のタイトルだよー",
        "link" : "記事のURLだよー"
    })


#def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)