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


def get_province():
    url = "https://www.anjuke.com/fangjia/"
    proxy = getProxy()
    html = getHTML(url,proxy)
    province = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/text()')
    url = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/@href')
    with open(os.getcwd() + "/data/info/province_url.txt", "w+", encoding='utf-8') as f:
        for i in range(1,27):
            f.write(province[i] + ',' + url[i] + '\n')


def get_city():
    f = open(os.getcwd() + "/data/info/province_url.txt", "r", encoding='utf-8')
    lines = f.read().split('\n')
    f.close()

    f = open(os.getcwd() + "/data/info/city_url2.txt", "a+", encoding='utf-8')
    for line in lines:
        province = line.split(',')[0]
        print('|-当前省份：{0}'.format(province))
        url = line.split(',')[1].split('\n')[0]
        html = getHTML(url, updateProxy())

        city = html.xpath('/html/body/div[2]/div[2]/div/span[2]/div/a/text()')
        city_url = html.xpath('/html/body/div[2]/div[2]/div/span[2]/div/a/@href')
        if province == '吉林' or province == '海南':
            city = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/text()')
            city_url = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/@href')

        info = []
        for i in range(len(city)):
            info.append('{0},{1},{2}'.format(province,city[i],city_url[i]))
        info = set(info)
        for i in info:
            f.write('{0}\n'.format(i))
            print('|城市：{0}'.format(i))
        print('--{0}完毕'.format(province))
        sleep(5)
    f.close()


def get_region():
    f = open(os.getcwd() + "/data/info/city_url.txt", "r", encoding='utf-8')
    lines = f.read().split('\n')
    f.close()

    for line in lines:
        line = line.split(',')
        print('|-当前城市：{0}'.format(line[1]))
        f = open(os.getcwd() + "/data/{0}_url.txt".format(line[0]), "a+", encoding='utf-8')
        html = getHTML(line[2], updateProxy())

        if line[1] == '盐城':

            region = html.xpath('/html/body/div[2]/div[2]/div/span[2]/div/a/text()')
            region_url = html.xpath('/html/body/div[2]/div[2]/div/span[2]/div/a/@href')
            for i in range(1,len(region)):
                f.write('{0},{1},{2},{3}\n'.format(line[0], line[1], region[i], region_url[i]))
                print('|区域：{0}'.format(region[i]))
        elif line[1] == '武汉':
            region = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/text()')
            region_url = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/@href')
            for i in range(1,len(region)):
                f.write('{0},{1},{2},{3}\n'.format(line[0], line[1], region[i], region_url[i]))
                print('|区域：{0}'.format(region[i]))


        else:
            region = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/text()')
            region_url = html.xpath('/html/body/div[2]/div[2]/div/span[2]/a/@href')
            for i in range(len(region)):
                f.write('{0},{1},{2},{3}\n'.format(line[0],line[1],region[i],region_url[i]))
                print('|区域：{0}'.format(region[i]))
        print('--{0}完毕'.format(line[1]))
        sleep(2)
        f.close()





if __name__ == '__main__':
    # get_province()
    # get_city()
    get_region()

