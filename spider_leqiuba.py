# -*- coding: utf-8 -*-
import requests
from lxml import html
import sys
from bs4 import BeautifulSoup
import re

print sys.getdefaultencoding()

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
douban_url = "http://www.leqiuba.cc/"

content = requests.get(douban_url, headers=head)
content.encoding = 'utf-8'
html_source = content.content
html_source = html_source.replace("\\", "")

selector = html.fromstring(html_source)

soup = BeautifulSoup(html_source, 'lxml')

# 根据关键字,抓取一场比赛
items = soup.find_all('div', class_='match_list')
emailid_regexp = re.compile(u".*中国.*")
match_info = soup.find(text=emailid_regexp).parent.parent.parent
aa = match_info.a.get('href')

# 再去爬取里面的信息
content2 = requests.get(aa, headers=head)
content2.encoding = 'utf-8'
html_source2 = content2.content
selector2 = html.fromstring(html_source2)
soup2 = BeautifulSoup(html_source2, 'lxml')

a_div = soup2.find('div', class_='switch')
aaaa = a_div.find_all('a')
ret = []
for a in aaaa:
    onclick = a.get('onclick')
    res = onclick.split(',')
    type = res[1]
    vid = res[2]
    type1 = type.replace("\'", "")
    vid2 = vid.replace("\'", "").replace("\')\'", "")
    ret.append(dict(type=type1, vid=vid2, v_name=a.string))

    print aa
