#!/usr/bin/python

import pycurl

try:
    from urllib.parse import urlencode
except ImportError:
        from urllib import urlencode

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from bs4 import BeautifulSoup

URL = "https://bitcointalk.org/index.php?board=159.0"


def get_method(curl, url):
    buffer = StringIO()
    curl.setopt(curl.URL,url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.setopt(curl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; Win64; x64;en; rv:5.0) Gecko/20110619 Firefox/5.0")
    curl.perform()
    curl.close()
    body = buffer.getvalue()
    return body

c = pycurl.Curl()
content = get_method(c, URL)


soup = BeautifulSoup(content, 'html.parser')
anchors = soup.findAll('a')

anchrList = []
for anchr in anchors:
    try:
        if 'topic' in anchr['href'] and anchr['href'].endswith('0'):
            anchrList.append(anchr['href'])
    except:
        pass


for anchor in anchrList:
    c = pycurl.Curl()
    content = get_method(c, anchor)
    if 'mining' in content:
        print(anchor)
