# -*- coding: utf-8 -*-
import requests
from lxml import html
import sys
from bs4 import BeautifulSoup
import re

print sys.getdefaultencoding()
# -*- coding: utf-8 -*-
import requests
from lxml import html
import sys
from bs4 import BeautifulSoup
import re

print sys.getdefaultencoding()

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
# douban_url = "http://www.leqiuba.cc/"
douban_url = "http://www.wuchajian.com/"
content = requests.get(douban_url, headers=head)
content.encoding = 'utf-8'
html_source = content.content
html_source = html_source.replace("\\", "")

selector = html.fromstring(html_source)

soup = BeautifulSoup(html_source, 'lxml')

# 根据关键字,抓取一场比赛
# emailid_regexp = re.compile(u"巴塞罗那")
# match_info = soup.find(text=emailid_regexp).parent.parent.parent.parent
# td_live_link = match_info.find('td', class_='live_link')
# many_a = td_live_link.find_all('a')
# # 再去爬取里面的信息
# for a in many_a:
#     href = a.get('href')
#     print href, a.string

emailid_regexp = re.compile(u".* 欧冠1/4决赛抽签仪式.*")
infos = soup.findAll(text=emailid_regexp)
for i in infos:
    match_info = i.parent.parent
    td_live_link = match_info.find('td', class_='live_link')
    many_a = td_live_link.find_all('a')
    # 再去爬取里面的信息
    for a in many_a:
        href = a.get('href')
        print href, a.string

