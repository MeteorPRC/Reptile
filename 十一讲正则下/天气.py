import re
import requests
import csv
import time

'''
获取页面的歌名，歌手名
'''


def source(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    print(html)
    return html


# 获取信息内容
def content(html):
    pass


# 保存
def save():
    pass


def main():
    url = "http://www.weather.com.cn/weather/101090201.shtml"
    html = source(url)
    # content(html)


if __name__ == '__main__':
    main()
