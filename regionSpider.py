from util.headers import *
from util.scrawl import *
import http.cookiejar
import urllib
from urllib.request import urlopen, Request
from lxml import etree
import codecs
import os
import json
from time import sleep

info_file = os.getcwd() + "/cityname.csv"

'''
保存 城市:url 数据
'''
def getCityUrl():
    url = "https://www.anjuke.com/sy-city.html"
    # cj = http.cookiejar.CookieJar()
    # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    # headers = create_headers()
    # opener.addheaders = headers
    # req = Request(url)
    #
    # data = urlopen(req).read().decode('utf8')
    # html = etree.HTML(data)
    html = getHTML(url)

    with codecs.open(info_file, "a+", 'utf-8') as f:
        for i in range(1,23):
            index = 1
            while True:
                city_xpath = "/html/body/div[3]/div/div[2]/ul/li[{0}]/div/a[{1}]/text()".format(i, index)
                url_xpath = "/html/body/div[3]/div/div[2]/ul/li[{0}]/div/a[{1}]/@href".format(i, index)
                try:
                    city = html.xpath(city_xpath)
                    url = html.xpath(url_xpath)
                    f.write(city[0] + ',' + url[0] + '\n')
                    print(city[0] + ',' + url[0])
                    index += 1
                except:
                    break

def getInfoUrl():
    file = codecs.open(info_file, 'r', 'utf-8')
    lines = [line.strip() for line in file]
    file.close()
    proxy = updateProxy()
    i = 0;
    with open(os.getcwd() + "/data/info/info_url.txt","w+",encoding='utf-8') as f:
        while i < len(lines):
            print("第{0}个城市".format(str(i)))
            url = lines[i].split(',')[1] + '/loupan/'
            ele = None
            try:
                ele = getHTML(url, proxy)
            except:
                proxy = updateProxy()
                continue
            try:
                url = ele.xpath('//*[@id="glbNavigation"]/div/ul/li[2]/a/@href')[0]
            except:
                proxy = updateProxy()
                print("进入验证")
                continue
            try:
                ele = getHTML(url, proxy)
            except:
                proxy = updateProxy()
                continue
            try:
                info_url = ele.xpath('//*[@id="container"]/div[7]/div[1]/div/div/a[6]/@href')[0]
                i += 1
            except:
                print("进入验证")
                proxy = updateProxy()
                continue


def createDict():
    city_dict = {}
    file = codecs.open(info_file, 'r', 'utf-8')
    lines = [line.strip() for line in file]
    for line in lines:
        city = line.split(',')[0]
        pinyin = line.split(',')[1].split('//')[1].split('.')[0]
        city_dict[city] = pinyin

    json_str = json.dumps(city_dict, indent=4, ensure_ascii=False)
    with open(os.getcwd() + "/data/info/city_dict.json", 'w+', encoding='utf-8') as jf:
        jf.write(json_str)
    file.close()

def getCityNameDict():
    with open(os.getcwd() + "/data/info/city_dict.json", 'r', encoding='utf-8') as f:
        str = f.read()
        return json.loads(str)




if __name__ == '__main__':
    # getCityUrl()
    # createDict()
    getInfoUrl()
