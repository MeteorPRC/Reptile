import requests
from bs4 import BeautifulSoup
import csv
import time

# 响应源
def source(url):
    header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    response=requests.get(url,headers=header)
    html= response.content.decode('utf-8')
    # print(html)
    return html

#筛选数据
def data(html):
    souplist=[]
    soup=BeautifulSoup(html,'lxml')
    soup_id=soup.select('div#AudioList')[0]
    # print(soup_id)
    soup_div=soup_id.select('div.audio-item')
    # print(soup_div,len(soup_div))
    for soupdiv in soup_div:
        soupdict={}
        # print(soupdiv)
        soup_class=soupdiv.select('div.right-head')[0]
        # print(soup_class)
        # time.sleep(6)
        soup_a=soup_class.select('a')[0]
        # print(soup_a)
        # time.sleep(6)
        url=soup_a.get('href')
        name=list(soup_a.p.stripped_strings)[0]
        print(name)
        # time.sleep(6)
        soupdict['name']=name
        soupdict['url']=f'https://sc.chinaz.com{url}'
        # print(soupdict)
        souplist.append(soupdict)
    # print(souplist)
    return souplist



# 保存数据
def save(souplist,i):
    headers = ['name', 'url']
    if i ==1:
        mod='w'
    else:
        mod='a'
    with open('音效.csv', mod, encoding='utf-8-sig', newline='') as f:
        writers = csv.DictWriter(f, headers)
        if i==1:
            writers.writeheader()
        writers.writerows(souplist)


# 主函数
def main():
    start=int(input('请输入起始页：'))
    end=int(input('请输入结束页：'))
    for i in range(start,end+1):
        if i ==1:
            index='index'
        else:
            index=f'index_{i}'
        url=f'https://sc.chinaz.com/yinxiao/{index}.html'
        html=source(url)
        souplist=data(html)
        save(souplist,i)


if __name__=='__main__':
    main()