# from bs4 import BeautifulSoup
# import requests
# import json
# import pprint
#
# headers={
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
#
# }
#
# url_paths=['https://www.pexels.com/search/table/?page={}/'.format(str(i)) for i in range(0,10)]
# path='/Users/sikezheng/Pictures/downloads/'    #要在路径最后加上/
#
# for url_path in url_paths:
#     wb_data=requests.get(url_path,headers=headers)
#     soup=BeautifulSoup(wb_data.text,'lxml')
#     # print(wb_data.text)
#     imgs=soup.select('div.page-wrap > div.l-container > div.photos > article > a:nth-of-type(2)') # a:nth-of-tpye(2)代表第二个a标签，只选中第二个a标签
#     list=[]
#     # print(imgs)
#     for img in imgs:
#         photo=img.get('href')
#         list.append(photo)
#     # pprint.pprint(imgs)
#     # pprint.pprint(list)
#     for item in list:
#         data=requests.get(item,headers=headers)
#         # print(data.content)
#         fp=open(path+item.split('?')[0][-10:],'wb')
#         fp.write(data.content)
#         fp.close()

############################Photo gettting

# import requests
# from bs4 import BeautifulSoup
#
# headers1={
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
# }
#
# urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))for i in range(0,20)]
#
# for url in urls:
#     res = requests.get(url, headers=headers1)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     price = soup.select(
#         '#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')  # 要将nth-child改为nth-of-type
#     for price1 in price:
#         print(price1.get_text())

############################Info gettting

# import requests
# from bs4 import BeautifulSoup
# import time
#
#
# headers1={
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
# }
#
# def geturlinfo(url):
#     wbdata1=requests.get(url,headers=headers1)
#
#     soup=BeautifulSoup(wbdata1.text,'lxml')
#     titles=soup.select('div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em') #要将selector前的body删除
#     adds=soup.select('div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
#     prices=soup.select('#pricePart > div.day_l > span')
#
#     for title,add,price in zip(titles,adds,prices):
#         data={
#             'title':title.get_text().strip(),
#             'add':add.get_text().strip(),
#             'price':price.get_text().strip()
#         }
#         print(data)
#
# def get_links(url):
#
#     wbdata=requests.get(url,headers=headers1)
#     soup=BeautifulSoup(wbdata.text,'lxml')
#
#     links=soup.select('#page_list > ul > li > a')
#     for link in links:
#         href=link.get("href")
#         geturlinfo(href)
#
#
#
#
# if __name__=='__main__':
#
#     urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(0,10)]
#     for surl in urls:
#         get_links(surl)
#         time.sleep(2)

############################details gettting

import requests
from bs4 import BeautifulSoup
import pprint

# url='https://www.pexels.com/popular-searches/?page=2&format=js&seed=1690371337'
# url1='https://www.pexels.com/popular-searches/'
# urls=['https://www.pexels.com/popular-searches.js?page={}&seed=1690371337&format=js&seed=1690371337'.format(str(i)) for i in range(3,10)]
# url='https://www.pexels.com/popular-searches/'
# L=[]
# L.append(url1)
# # L.append(url)
# L.append(urls)
url='https://www.pexels.com/popular-searches.js?page=3&seed=1690371337&format=js&seed=1690371337'
# print(L)

headers={
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

}

wbdata=requests.get(url,headers=headers)
print(wbdata.text)


# for url in L:
#     wbdata=requests.get(url,headers=headers)
#     soup=BeautifulSoup(wbdata.text,'lxml')
#         # print(soup)
#     name1=soup.select('div.l-lg-3.l-md-4.l-sm-6 > a.search-medium__link > h4.search-medium__title')
#         # pprint.pprint(soup)
#
#     for name in name1:
#         print(name.get_text())

    # for name in name1:
        # print(name.get_text())
        # L.append(name.get_text())

# print(len(L))

