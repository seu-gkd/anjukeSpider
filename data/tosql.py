import os
with open('alldata.csv','a+',encoding='utf-8') as target:
    count = 0
    target.write('year,mouth,province,city,citylevel,longitude,twist,houseprice,proportion,inc,inc_2,pricehistoryId\n')
    provinces = ['直辖市','江苏','安徽','福建','甘肃','广东','广西','贵州','河北','河南','黑龙江','湖北','湖南','江西','辽宁','内蒙古','宁夏','青海','山东','山西','陕西','四川','西藏','新疆','云南','浙江']
    for province in provinces:
        with open(os.getcwd() + "/region/{}_info.txt".format(province), 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
            if data[-1] == '':
                data.pop()
            for item in data:
                i = item.split(',')
                year = i[3].split('年')[0]
                mouth = i[3].split('年')[0] + '-' + i[3].split('年')[1].split('月房价')[0]
                mouth = str(mouth)
                province = i[0]
                city = i[1]
                citylevel = i[2]
                longitude = '0'
                twist = '0'
                houseprice = i[4].split('元')[0]
                try:
                    proportion = str(round(float(i[5].split('%')[0])/100,4))
                    inc = i[5].split('%')[1]
                    if inc == '↑':
                        inc_2 = '上升'
                    else:
                        inc_2 = '下降'
                except:
                    proportion = '--'
                    inc = ''
                    inc_2 = '持平'
                pricehistoryId = str(count)
                count += 1
                w = str(year + ',' + mouth + ',' + province + ',' + city + ',' + citylevel + ',' + longitude + ',' + twist + ',' + houseprice + ',' + proportion + ',' + inc + ',' + inc_2 + ',' + pricehistoryId + '\n')
                print(w)
                target.write(w)