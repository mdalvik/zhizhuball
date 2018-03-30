# -*- coding: utf-8 -*-
import requests
import sys, json, redis
import datetime
from dateutil import parser

print sys.getdefaultencoding()

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
urls = []
# 英超
url_Premier = "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=3"
# 西甲
url_laliga = "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=43"
# 德甲
url_bundesliga = "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=65"
# 意甲
url_SerieA = "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=7"
# 法甲
url_Ligue1 = "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=19"
# 欧冠
url_UEFA = "http://sports.pptv.com/interface/pg_2016live?cb=p&competitionid=45"

urls.append(url_Premier)
urls.append(url_laliga)
urls.append(url_bundesliga)
urls.append(url_SerieA)
urls.append(url_Ligue1)
urls.append(url_UEFA)

ret = []
for url in urls:
    content = requests.get(url, headers=head)
    content.encoding = 'utf-8'
    html_source = content.content
    html_source = html_source.replace("p(", "")
    html_source = html_source.replace(");", "")
    # print html_source
    bean = json.loads(html_source)
    data = bean.get('data')
    server_time = data.get('server_time')
    dateArray = datetime.datetime.now()
    local_time = dateArray.strftime("%m-%d")
    matches = data.get('list')
    # print local_time

    for m in matches:
        show_time = m.get('show_time')
        datetime_struct = parser.parse(show_time)
        show_time_ = datetime_struct.strftime('%m-%d')
        # print show_time_
        if show_time_ == local_time:
            ret.append(m)



