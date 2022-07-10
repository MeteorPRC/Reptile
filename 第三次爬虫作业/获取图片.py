import requests
from bs4 import BeautifulSoup
import csv
import time

# 响应源
def source(url):
    header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    response=requests.get(url,headers=header)     #响应
    html=response.content.decode('utf-8')
    # print(html)
    return html
#筛选数据
def data(html):
    souplist=[]
    soup=BeautifulSoup(html,'lxml')
    soup_div=soup.find_all('div',id="container")[0]
    # print(soup_div)
    soup_div2=soup_div.find_all('div',class_="box picblock col3")
    # print(soup_div2,len(soup_div2))
    for soupdiv in soup_div2:
        soupdict={}
        # print(soupdiv)
        soup_p=soupdiv.find('p')
        # print(soup_p)
        # time.sleep(5)  #测试
        soup_a=soup_p.find('a')
        # print(soup_a)
        href=soup_a['href']
        name=soup_a.string
        # print(href,name)
        url=f'https:{href}'
        # print(url)
        soupdict['name'] = name
        soupdict['url']=url
        # print(soupdict)
        souplist.append(soupdict)
    # print(souplist)
    return souplist

# 保存数据
def save(souplist,i):
    headers=['name','url']
    if i ==1:
        mod='w'
    else:
        mod='a'
    with open('图册.csv',mod,encoding='utf-8-sig',newline='')as f:
        writers=csv.DictWriter(f,headers)
        if i==1:
            writers.writeheader()
        writers.writerows(souplist)








# 主函数
def main():
    start=int(input('请输入起始页：'))
    end=int(input('请输入结束页：'))
    for i in (start,end+1):
        if i==1:
            index='index'
        else:
            index=f'index_{i}'
        url=f'https://sc.chinaz.com/tupian/{index}.html'
        html=source(url)
        souplist=data(html)
        save(souplist,i)

# 程序主入口
if __name__ =='__main__':
    main()