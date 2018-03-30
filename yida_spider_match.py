# -*- coding: utf-8 -*-
from flask import Flask, render_template

import requests
from lxml import html
import sys, json, redis
from bs4 import BeautifulSoup
from flask_redis import FlaskRedis

app = Flask(__name__)

r = FlaskRedis(app=app)


@app.route('/')
def hello_world():
    return render_template('pages/index.html')


@app.route('/spider')
def spider():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    urls = []
    # 英超
    url_Premier = {"Premier": "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=3"}
    # 西甲
    url_laliga = {"laliga": "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=43"}
    # 德甲
    url_bundesliga = {"bundesliga": "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=65"}
    # 意甲
    url_SerieA = {"SerieA": "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=7"}
    # 法甲
    url_Ligue1 = {"Ligue1": "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=19"}
    # 欧冠
    url_UEFA = {"UEFA": "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=45"}

    urls.append(url_Premier)
    urls.append(url_laliga)
    urls.append(url_bundesliga)
    urls.append(url_SerieA)
    urls.append(url_Ligue1)
    urls.append(url_UEFA)

    for url in urls:
        for k, v in url.iteritems():
            content = requests.get(url[k], headers=head)
            content.encoding = 'utf-8'
            html_source = content.content
            html_source = html_source.replace("p(", "")
            html_source = html_source.replace(");", "")
            r.set(k, html_source)
            print html_source

    return 'ok!'


@app.route('/getPremier')
def getPremier():
    Premier = r.get("Premier")
    return Premier


if __name__ == '__main__':
    app.run()
