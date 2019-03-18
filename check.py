import pymysql
import os
import json
from scrawl import *
from dataSpider import *


def check():
    db = pymysql.connect("47.101.44.55", "root", "gkd123,.", "Houseprice", use_unicode=True, charset='utf8')
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT province from pricehistorynew")
    data = cursor.fetchall()

    provinces = []
    for i in data:
        provinces.append(i[0])

    city_sql = "select DISTINCT city from pricehistorynew where province = '{0}'"
    region_sql = "select DISTINCT citylevel from pricehistorynew where city = '{0}'"
    year_sql = "select DISTINCT `year` from pricehistorynew where citylevel = '{0}'"

    for province in provinces:
        cursor.execute(city_sql.format(province))
        data = cursor.fetchall()
        cities = []
        for i in data:
            cities.append(i[0])
        for city in cities:
            if city == '无':
                continue
            cursor.execute(region_sql.format(city))
            data = cursor.fetchall()
            regions = []
            for i in data:
                regions.append(i[0])
            for region in regions:
                if region == '无':
                    continue
                cursor.execute(year_sql.format(region))
                data = cursor.fetchall()
                years = []
                for i in data:
                    years.append(i[0])
                for i in range(min(years),max(years)):
                    if i not in years:
                        with open('check.txt','a+', encoding='utf-8') as f:
                            f.write(province + ',' + city + ',' + region + ',' + str(i) + '\n')

def repay():
    with open('check.txt','r',encoding='utf-8') as f:
        data = f.read()
        data = data.split('\n')
    with open(os.getcwd() + "/data/info/city_dict.json", 'r', encoding='utf-8') as f:
        dict = json.loads(f.read())

    urls = []
    provinces = ['直辖市','江苏','安徽','福建','甘肃','广东','广西','贵州','河北','河南','黑龙江','湖北','湖南','江西','辽宁','内蒙古','宁夏','青海','山东','山西','陕西','四川','新疆','云南','浙江']
    for province in provinces:
        f = open(os.getcwd() + "/data/{}_url.txt".format(province), 'r', encoding='utf-8')
        temp = f.read().split('\n')
        if temp[-1] == '':
            temp.pop()
        urls += temp
    for i in data:
        for url in urls:
            ti = i.split(',')
            tu = url.split(',')
            if ti[0] == tu[0] and ti[1] == tu[1] and ti[2] == tu[2]:
                temp = tu[3].split(dict[tu[1]])
                url = temp[0] + dict[tu[1]] + str(ti[3]) + temp[1]
                with open(os.getcwd() + "/data/repay/repay_url.txt", 'a+', encoding='utf-8') as target:
                    target.write(ti[3] + ',' + ti[0] + ',' + ti[1] + ',' + ti[2] + ',' + url + '\n')

def get():
    with open(os.getcwd() + "/data/repay/repay_url.txt", 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
    for i in data:
        html = getHTML(i.split(',')[4], get_proxy())
        date, price, gr = analyse_city_html(html)
        for idx in range(len(date)):
            temp = i.split(',')
            with open(os.getcwd() + "/data/repay/repay_data.txt", 'a+', encoding='utf-8') as f:
                f.write(temp[1] + ',' + temp[2] + ',' + temp[3] + ',' + date[idx] + ',' + price[idx] + ',' + gr[idx] + '\n')
                print(temp[1] + ',' + temp[2] + ',' + temp[3] + ',' + date[idx] + ',' + price[idx] + ',' + gr[idx] + '\n')




if __name__ == '__main__':
    # check()
    # repay()
    get()