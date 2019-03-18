import os

with open('repay.csv','a+',encoding='utf-8') as target:
    count = 100000
    with open('repay_data.txt', 'r', encoding='utf-8') as f:
        repay_data = f.read().split('\n')
        if repay_data[-1] == '':
            repay_data.pop()
        for item in repay_data:
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
                proportion = str(round(float(i[5].split('%')[0]) / 100, 4))
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
            w = str(
                year + ',' + mouth + ',' + province + ',' + city + ',' + citylevel + ',' + longitude + ',' + twist + ',' + houseprice + ',' + proportion + ',' + inc + ',' + inc_2 + ',' + pricehistoryId + '\n')
            print(w)
            target.write(w)
