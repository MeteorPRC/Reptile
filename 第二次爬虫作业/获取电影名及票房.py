import requests
import csv
from lxml import etree
'''
7.(必做题1)目标网站：http://www.piaofang.biz/
需求：
1、爬取页面所有电影名及票房
2、保持到csv问答题 0.0分
'''
# 获取网页源代码
def getsource(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding = 'gb2312'
    html = response.text
    # print(html)
    return html


# 获取网页源代码中的电影名及票房
def geteveryitem(html):
    element=etree.HTML(html)
    movieitemlist=element.xpath('//tr//td[@class="title"]')
    print(movieitemlist)
    movelist=[]
    for item in movieitemlist:
        movedict={}
        # 电影名
        name=item.xpath('./a/text()')
        if name:
            name=name[0]
        else:
            continue
        # print(name)
        # 票房
        piaofang=item.xpath('../td[@class="piaofang"]/span/text()')[0]
        # print(piaofang)
        movedict['name']=name
        movedict['piaofang']=piaofang
        movelist.append(movedict)
    # print(movelist)
    return movelist
# 保存信息.csv格式

def writeData(movelist):
    with open('电影票房排行榜.csv','w',encoding='utf-8-sig',newline='')as f:
        writer=csv.DictWriter(f,fieldnames=['name','piaofang'])
        writer.writeheader()
        writer.writerows(movelist)



if __name__ == '__main__':
    url='http://www.piaofang.biz/'
    html=getsource(url)
    movelist=geteveryitem(html)
    writeData(movelist)