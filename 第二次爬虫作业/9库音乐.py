import requests
import csv
from lxml import etree

'''
8.(必做题2)目标网站：https://www.9ku.com/music/t_new.htm
需求：
1、爬取到榜单页面使有的歌曲名、歌曲地址
2、保存到csv
https://www.9ku.com/music/t_new.htm
'''


# 定义一个函数用来获取网页源代码
def getsource(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    return html


def geteveryitem(html):
    element = etree.HTML(html)
    '''
    孤勇着
    /html/body/div[@class='bangBox clearfix']/div[@class='bangR']/div[@class='mdBox bgWrite']/div[@class='mdBoxBd']/form/div[@id='body']/div[@id='f1']/ol/li[1]/a[@class='songName ']
    踏山河
    /html/body/div[@class='bangBox clearfix']/div[@class='bangR']/div[@class='mdBox bgWrite']/div[@class='mdBoxBd']/form/div[@id='body']/div[@id='f2']/ol/li[1]/a[@class='songName ']
    '''
    music = element.xpath('//form/div[@id="body"]/div[@class="songList clearfix"]/ol/li/a')
    print(music)
    musiclist = []
    for item in music:
        musicdict = {}
        musicname = item.xpath("./text()")[0]
        # print(musicname)
        musicurll = item.xpath("./@href")[0]
        # print(musicurll)
        musicurl = 'https://www.9ku.com' + musicurll
        # print(musicurl)
        musicdict['musicname'] = musicname

        musicdict['musicurl'] = musicurl
        musiclist.append(musicdict)
    print(musiclist)
    return musiclist


def writeData(musiclist):
    with open('9ku音乐.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['musicname','musicurl'])
        writer.writeheader()
        writer.writerows(musiclist)


if __name__ == '__main__':
    url = 'https://www.9ku.com/music/t_new.htm'
    html = getsource(url)
    musiclist = geteveryitem(html)
    writeData(musiclist)
