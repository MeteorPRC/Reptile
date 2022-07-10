from bs4 import BeautifulSoup
import requests
import csv
'''
url='http://www.weather.com.cn/textFC/hb.shtml'
'''
# 获取源码
def source(url):
    html=requests.get(url)
    html=html.content.decode('utf-8')
    return html

# 用bs4获取信息
def obtain(html):
    templist=[]
    soup=BeautifulSoup(html,'lxml')
    conMidtab=soup.find_all('div',attrs={'class':'conMidtab'})[0]
    # print(conMidtab)
    tables=conMidtab.find_all('table')
    # print(tables)
    for table in tables:
        # print(table)
        trs=table.find_all('tr')[2:]
        # print(trs)
        for tr in trs:
            tempdict={}
            tds=tr.find_all('td')
            # print(tds)
            # 城市
            city_td=tds[0]
            # print(city_td)
            city=list(city_td.stripped_strings)[0]
            # city=city_td.stripped_strings
            # print(city)
            # 天气温度
            temp_td=tds[-2]
            temp=list(temp_td.stripped_strings)[0]
            # print(temp)
            tempdict['city']=city
            tempdict['temp']=temp
            print(tempdict)
            templist.append(tempdict)
    return templist



# 用csv保存信息
def save(temolist):
    with open('天气预报.csv','w',encoding='utf-8-sig',newline='') as f :
        writers=csv.DictWriter(f,fieldnames={'city','temp'})
        writers.writeheader()
        writers.writerows(temolist)



# 程序主入口
if __name__=='__main__':
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    html=source(url)
    templist=obtain(html)
    save(templist)