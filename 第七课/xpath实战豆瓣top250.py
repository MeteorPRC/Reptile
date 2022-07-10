import csv
import requests
from lxml import etree

'''
目标：熟悉xpath解析数据的方式
需求： 爬取电影名称    评分   引言            详情页的uel 翻页进行爬取1-10页的内容 并保存到csv文件中
        title      score   introduction    url
解决方案： requests lxml csv 
'''

'''
网址解析：
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=75&filter=
'''
# start=int(input('请输入开始页：'))
# end=int(input('请输入结束页：'))
# for i in range(start,end+1):
#     url=f'https://movie.douban.com/top250?start={(i-1)*25}&filter='



# 定义一个函数用来获取网页源代码
def getsource(url):

    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    # print(html)
    return html

# 定义一个函数用来皆学问i网站也源代码
def geteveryitem(html):
    element=etree.HTML(html)
    # print(element)
    movieitemlist=element.xpath("//li[@class='list_item__3gOKl']/div[@class='tw-py-16 tw-pr-12']")
    print(movieitemlist)
    itemlist=[]
    for item in movieitemlist:
        # 定义字典
        itemdict={}
        # 标题
        title=item.xpath("./div[@class='hd']/a/span[@class='title']/text()")[0]
        # print(title)
        # 评分
        scoree=item.xpath('./div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        # print(scoree)
        # url
        link=item.xpath('./div[@class="hd"]/a/@href')[0]
        # print(link)
        # 引言
        quote=item.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')
        #对quote进行处理
        # 处理方式： 非空判断
        if quote:
            quote=quote[0]
        else:
            quote=''
        # print(quote)
        itemdict['title']=title
        itemdict['quote']=quote
        itemdict['score']=scoree
        itemdict['link']=link
        itemlist.append(itemdict)
    # print(itemlist)
    return itemlist

# 定义一个函数用来将我们解析到的数据进行报讯
def writeData(itemlist):
    with open('豆瓣Top250.csv','w',encoding='utf-8-sig',newline='') as f:
        #创建writer对象
        writer=csv.DictWriter(f,fieldnames=['title','quote','score','link'])
        writer.writeheader()
        for i in itemlist:
            writer.writerow(i)


# 程序主入口，调用函数
if __name__ == '__main__':
    movieadddatalist=[]
    for x in range(10):
        url = f'https://movie.douban.com/top250?start={x*25}&filter='
        html=getsource(url)
        # print(html)
        itemlist=geteveryitem(html)
        movieadddatalist+=itemlist
    writeData(movieadddatalist)