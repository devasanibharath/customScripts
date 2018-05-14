import pycurl
from faker import Faker
from random import randint
import time
IP = "5.167.54.154"
PORT = "8080"

fckr = Faker()

try:
    from urllib.parse import urlencode
except ImportError:
        from urllib import urlencode


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

URL="#"


def get_method(curl, url):
    buffer = StringIO()
    curl.setopt(curl.URL,url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()
    body = buffer.getvalue()
    print(body)

def post_method(curl, url, argument):
    curl.setopt(curl.URL,url)
    post_data = argument
    postfields = urlencode(post_data)
    curl.setopt(curl.POSTFIELDS, postfields)
    # curl.setopt(pycurl.HTTPHEADER,['Content-Type: application/json'])
    curl.setopt(pycurl.PROXY, "%s:%s" % (IP, PORT))
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
    curl.setopt(curl.VERBOSE, False)
    curl.setopt(curl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; Win64; x64;en; rv:5.0) Gecko/20110619 Firefox/5.0")
    curl.perform()
    curl.close()

def main():
    c = pycurl.Curl()
    post_method(c, URL, {"text17":fckr.name(), "email18": fckr.email(), "tel19": str(randint(6000000000, 9999999999)), "select21" : 1,"select22": 1,"d1": "31/03/2018", "d2": "01/04/2018", "select25": "Standard Room","select26": 2,"textarea30": fckr.text(), "fb_js_enable": 1, "fb_form_custom_html": "", "fb_form_embedded": "", "fb_url_embedded": ""})

#
main()
i = 0
while i < 1000:
    try:
        main()
        i +=1
        print("[+] Posting Request Number ",i)
        # time.sleep(1)
    except:
        i -=1
