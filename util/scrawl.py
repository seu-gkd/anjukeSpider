from util.headers import *
import http.cookiejar
import urllib
from urllib.request import urlopen, Request
from lxml import etree
from proxy import *
import requests

# def getHTML(url):
#
#     cj = http.cookiejar.CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     headers = create_headers()
#     opener.addheaders = headers
#     req = Request(url)
#     data = urlopen(req).read().decode('utf8')
#     return etree.HTML(data)


def getHTML(url, proxy=None):
    rsp = get(url, proxy)
    while rsp is None or rsp.text.find('访问验证') != -1:
        rsp = get(url, get_proxy())
    html = etree.HTML(rsp.text)
    return html


def get(url, proxy = None):
    if proxy is None:
        rsp = requests.get(url, headers=create_headers(url), timeout = 3)
        return rsp
    else:
        try:
            rsp = requests.get(url, proxies=proxy, headers=create_headers(url), timeout=3)
            return rsp
        except:
            return None
