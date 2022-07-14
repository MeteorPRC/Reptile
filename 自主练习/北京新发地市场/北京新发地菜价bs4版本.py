"""
项目要求：bs4去获取北京新发地官网的蔬菜价格
日期：22/07/13
"""
import csv

import requests
from fake_useragent import UserAgent  # 随机请求头
from bs4 import BeautifulSoup

page = eval(input("下载第几页的信息"))
url = 'http://www.xinfadi.com.cn/getPriceData.html'
# http://www.xinfadi.com.cn/getPriceData.html
headers = {
    "User-Agent": UserAgent().chrome
}
data = {
    "limit": 20,
    "current": page
}
# ,data=data
response = requests.post(url, headers=headers, data=data)
# 数据信息解析
info = response.json()
# print(info,type(info))
# 菜
vegetable = info['list']
sclist=[]
# print(vegetable)
for item in vegetable:
    # print(item)
    # 种类
    scdict = {}
    prodCat = item['prodCat']
    # 蔡明
    prodName = item['prodName']
    # 最低价
    lowPrice = item['lowPrice']
    # 平均价
    avgPrice = item['avgPrice']
    # 最高价
    highPrice = item['highPrice']
    # 产地
    place = item['place']
    # 日期
    pubDate = item['pubDate']

    scdict['种类'] = prodCat
    scdict['蔡明'] = prodName
    scdict['最低价'] = lowPrice
    scdict['平均价'] = avgPrice
    scdict['最高价'] = highPrice
    scdict['产地'] = place
    scdict['日期'] = pubDate
    sclist.append(scdict)

header=['种类','蔡明','最低价','平均价','最高价','产地','日期']
with open('北京新发地蔬菜价格查询_数据包版.csv','w',encoding='utf-8-sig',newline='') as f :
    writer=csv.DictWriter(f,header)
    writer.writeheader()
    writer.writerows(sclist)
'''

        {'id': 1305138, 'prodName': '绿菜花', 'prodCatid': 1186, 'prodCat': '蔬菜', 'prodPcatid': None, 'prodPcat': '', 'lowPrice': '1.5', 'highPrice': '2.2', 'avgPrice': '1.85', 'place': '苏豫冀', 'specInfo': '', 'unitInfo': '斤', 'pubDate': '2022-07-13 00:00:00', 'status': None, 'userIdCreate': 138, 'userIdModified': None, 'userCreate': 'admin', 'userModified': None, 'gmtCreate': None, 'gmtModified': None}
'''
