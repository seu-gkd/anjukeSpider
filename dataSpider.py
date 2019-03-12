from util.proxy import *
from util.scrawl import *
import os
import json


def analyse_city_html(html):
    date = html.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/b/text()')
    price = html.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/span/text()')
    gr = html.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/em/text()')
    return date,price,gr


def get_city_data():
    f = open(os.getcwd() + "/data/info/city_url.txt", "r", encoding='utf-8')
    lines = f.read().split('\n')
    for line in lines:
        place = line.split(',http://www.anjuke.com/fangjia/')[0]
        city = line.split('/')[-2]
        url = "https://www.anjuke.com/fangjia/{0}{1}"
        for year in range(2010, 2020):
            html = getHTML(url.format(city,year), get_proxy())
            date, price, gr = analyse_city_html(html)
            with open(os.getcwd() + "/data/data/{}_info.txt".format(place.split(',')[0]), "a+", encoding='utf-8') as f:
                for i in range(len(date)):
                    f.write(place + ',' + date[i] + ',' + price[i] + ',' + gr[i] + '\n')
                print(place + ',' + str(year) + ',done')
    pass


def get_region_data():
    f = open(os.getcwd() + "/data/info/city_dict.json", 'r', encoding='utf-8')
    dict = json.loads(f.read())
    f.close()
    provinces = ['河南','黑龙江','湖北','湖南','江苏','江西','辽宁','内蒙古','宁夏','青海','山东','山西','陕西','四川','西藏','新疆','云南','浙江']
    for province in provinces:
        print(province)
        f = open(os.getcwd() + "/data/{0}_url.txt".format(province), "r", encoding='utf-8')
        lines = f.read().split('\n')
        if lines[-1] is '':
            lines.pop()
        for line in lines:
            if line.find('其他')!= -1 or line.find('周边')!= -1 or line.find('全部')!= -1:
                continue
            place = line.split(',http')[0]
            url = line.split('//')[1]
            temp = url.split(dict[place.split(',')[-2]])
            url = temp[0] + dict[place.split(',')[-2]] + '{0}' + temp[1]
            for year in range(2010,2020):
                html = getHTML("https://" + url.format(year), get_proxy())
                date, price, gr = analyse_city_html(html)

                with open(os.getcwd() + "/data/region/{}_info.txt".format(place.split(',')[0]), "a+",
                          encoding='utf-8') as f:
                    for i in range(len(date)):
                        f.write(place + ',' + date[i] + ',' + price[i] + ',' + gr[i] + '\n')
                    print(place + ',' + str(year) + ',done')

        f.close()
        pass


if __name__ == '__main__':
    # get_city_data()
    get_region_data()


