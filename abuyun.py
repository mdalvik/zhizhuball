# -*-*-
# -*-*-

# ! -*- encoding:utf-8 -*-
import threading
import requests

targetUrl = "http://www.zhizhuball.com"

proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

proxyUser = "H6066AE65P4EH41D"
proxyPass = "98403CED89850131"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}


def fun_timer():
    resp = requests.get(targetUrl, headers=head)
    print resp.status_code
    timer = threading.Timer(0.1, fun_timer)
    timer.start()


timer = threading.Timer(1, fun_timer)
timer.start()
