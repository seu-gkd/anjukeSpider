import requests
import random
from time import sleep
from lxml import etree
from util.headers import *

# def getProxy():
#     url = "https://www.xicidaili.com/"
#
#     req = Request(url)
#
#     req.add_header('User-Agent',
#                    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
#     data = urlopen(req).read().decode('utf8')
#     html = etree.HTML(data)
#     proxy_list = []
#     for i in range(47,60):
#         ip = html.xpath('//*[@id="ip_list"]/tr[{0}]/td[2]/text()'.format(i))[0]
#         port = html.xpath('//*[@id="ip_list"]/tr[{0}]/td[3]/text()'.format(i))[0]
#         proxy_list.append(ip + ':' + port)
#         pass
#     return proxy_list

def getProxy():
    proxy_url = [
        "http://api3.xiguadaili.com/ip/?tid=559715404442296&num=1000&operator=1&delay=3&area=安徽&protocol=https"
    ]
    rsp = requests.get(proxy_url[0])
    proxy_list = rsp.text.split('\r\n')
    return check_proxy(proxy_list)

    # rsp = requests.get(proxy_url[0], headers=create_headers(proxy_url[0]), timeout = 3)
    # html = etree.HTML(rsp.text)
    # ip = html.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
    # port = html.xpath('//*[@id="ip_list"]/tr/td[3]/text()')
    # proxy_list = []
    # for i in range(10):
    #     proxy_list.append(ip[i] + ':' + port[i])
    # return proxy_list

def check_proxy(proxy_list):
    count = 0
    while True:
        item = random.sample(proxy_list,1)
        count += 1
        proxies = {
            "https": "https://" + item[0]
        }
        try:
            rsp = requests.get("https://www.baidu.com", proxies=proxies, headers = create_headers(), timeout = 5)
            if rsp.text is not None:
                return proxies
                break
        except Exception:
            pass
        if count > 4:
            return None
    # for item in proxy_list:
    #     proxies = {
    #         "https": "https://" + item
    #     }
    #     try:
    #         rsp = requests.get("https://www.baidu.com", proxies=proxies, headers = create_headers(), timeout = 5)
    #         if rsp.text is not None:
    #             return proxies
    #             break
    #     except Exception:
    #         return None

def updateProxy():
    proxy = None
    while proxy is None:
        proxy = getProxy()
        sleep(2)
        if proxy is not None:
            print('proxy:' + proxy['https'])
            return proxy
            break
        print("获取代理失败，等待1秒")

def get_proxy():
    proxy = {
        "https": "https://" + requests.get("http://127.0.0.1:5010/get/").text
    }
    return proxy

if __name__ == '__main__':
    a = updateProxy()
    print(a)
