"""
制作人：18期爬虫-04-正则表达式-赵经纬
时间：2022-06-28
"""
import csv
import requests
import re
import time

# 获取源码score
def score(url):
    header={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response=requests.get(url,headers=header)
    html=response.content.decode('utf-8')
    # print(html)
    return html
# 筛查信息
def screening(html):
    movielist=[]
    re_div=re.findall(r'.*?(<main class="rel container_2VTvm">.*?</main>).*?',html)[0]
    # print(re_div)
    re_div2=re.findall('<div class="content_1YWBm">.*?</div>.*?</a>.*?</div>.*?</a>.*?</div>',re_div)
    # print(re_div2,len(re_div2))
    for re_divs in re_div2:
        # 电影名字 movie name
        moviedict={}
        moviename=re.findall('<div class="c-single-text-ellipsis">(.*?)</div>',re_divs)[0].replace(" ",'')
        print(moviename)
        moviedict['moviename']=moviename
        # 类型
        movietype=re.findall('<div class="intro_1l0wp">.*?类型：(.*?)</div>',re_divs)[0]
        print(movietype)
        moviedict['movietype']=movietype
        # 演员
        actor=re.findall('<div class="intro_1l0wp"> 演员：(.*?)</div>',re_divs)[0]
        print(actor)
        moviedict['actor']=actor
        movielist.append(moviedict)
    return movielist


'''
.*？<main class="rel container_2VTvm">.*？<div class="container-bg_lQ801">.*?</div></main>.*？
<div class="content_1YWBm">.*?</div>.*?</a>.*?</div>.*?</a>.*?</div>
'''
# 保存信息
def save(movielist):
    hrader=['moviename','movietype','actor']
    with open('百度电影热榜.csv','w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,hrader)
        writer.writeheader()
        writer.writerows(movielist)
        print('运行完成，正在退出....')
        time.sleep(5)

# 主函数
def main():
    url='https://top.baidu.com/board?tab=movie'
    html=score(url)
    movielist=screening(html)
    save(movielist)

# 程序主入口
if __name__=="__main__":
    main()