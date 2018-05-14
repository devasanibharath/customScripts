import pycurl
from faker import Faker

IP = "76.1.89.29"
PORT = "59378"

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
    # curl.setopt(pycurl.PROXY, "%s:%s" % (IP, PORT))
    # curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    curl.setopt(curl.VERBOSE, False)
    curl.setopt(curl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; Win64; x64;en; rv:5.0) Gecko/20110619 Firefox/5.0")
    curl.perform()
    curl.close()

# def main():
#     c = pycurl.Curl()
#     post_method(c, URL, {"name":fckr.name(), "email": fckr.email(), "subject": fckr.address(), "message" : fckr.text(), "submit": "Submit+Form"})
#
#
# main()
# i = 0
# while i < 1000:
#     main()
#     i +=1
#     print("[+] Posting Request Number ",i)
#     sleep(1)


c = pycurl.Curl()
get_method(c, "https://www.isac.gov.in/sahayak/CaptchaServlet")
