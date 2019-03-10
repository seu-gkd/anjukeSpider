import os

if __name__ == '__main__':
    f = open(os.getcwd() + "/miss.txt",'r', encoding='utf-8')
    miss_city = f.read().split('\n')
    f.close()

    f = open(os.getcwd() + "/data/info/city_url.txt", 'r', encoding='utf-8')
    urls = f.read().split('\n')
    f.close()
    for url in urls:
        if url.split(',')[1] not in miss_city:
            urls.remove(url)
            pass
    f = open(os.getcwd() + "/data/info/city_url.txt", 'w', encoding='utf-8')
    for url in urls:
        f.write(url + '\n')
    f.close()