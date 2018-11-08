import requests
import time
from bs4 import BeautifulSoup
import random
import pymongo

client=pymongo.MongoClient('localhost',27017)
mydb1=client['mydb1']
movietop=mydb1['movietop']


urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
# url='https://movie.douban.com/top250'
# proxies = {'http': '123.7.61.8:53281'}
cookies={'cookie':'bid=LmPZEEsFky4; __yadk_uid=dFNMqEaxCDhwp1CQ9I1ALT2XMcgzSqV2; gr_user_id=90e35bdb-152c-4963-a4e4-3f5da7872ee4; _vwo_uuid_v2=DAA90A0C617A4FAEEFE8482A698416486|e6e25f88e86f62d6751f99448c2fff29; ll="118286"; ct=y; douban-fav-remind=1; __utmc=30149280; viewed="2228378_11874748_10546125_26576861_10750155"; ap_v=0,6.0; ps=y; ue="zhengsikesiko@163.com"; push_noty_num=0; push_doumail_num=0; __utma=30149280.1489318586.1539875760.1541576933.1541581029.10; __utmz=30149280.1541581029.10.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1541581709%2C%22https%3A%2F%2Fmovie.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utmt=1; __utmv=30149280.8321; _pk_id.100001.8cb4=79bf7085ba7b0554.1539875759.6.1541581791.1541336951.; __utmb=30149280.5.10.1541581029; dbcl2="83212537:I5ESJ9zXGJk"'}
headers={
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
# for url in urls:
#
#     res=requests.get(url,headers=headers,cookies=cookies)
#     time.sleep(random.randint(0,5))
#     # print(res.text)



for url in urls:
    # print(url)
    res=requests.get(url,headers=headers,cookies=cookies) #伪造cookies
    # print('hi')
    time.sleep(random.randint(0, 5))   #防止请求过密
    soup=BeautifulSoup(res.text,'lxml')
    # print('hi')
    # print(soup)
    # fna=soup.find_all('span',class_='title')
    # print(fna)
    filmname=soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-of-type(1)')
    filmrate=soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')
    filmnum=soup.select('#content > div > div.article > ol > li > div > div.pic > em')

    for name1,rate1,num1 in zip(filmname,filmrate,filmnum):       #打包迭代一堆信息的时候，in后要用zip
        infos={
                'filmnam':name1.get_text(),
                'filmrate':rate1.get_text(),
                'filmnum':num1.get_text()
                }
        movietop.insert_one(infos)


