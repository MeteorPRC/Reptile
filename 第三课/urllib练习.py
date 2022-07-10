import urllib.parse
from urllib import request

'''
网址分析：
海贼王吧
https://tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=100
lol陪玩
https://tieba.baidu.com/f? kw=lol%E9%99%AA%E7%8E%A9 &ie=utf-8& pn=0
https://tieba.baidu.com/f? kw=lol%E9%99%AA%E7%8E%A9 &ie=utf-8& pn=50
'''
url='https://tieba.baidu.com/f?'
headers={
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}

name1=input('请输入你要搜索的贴吧名称：')
# 处理name（贴吧名称）
name=urllib.parse.quote(name1)
start=int(input('请输入起始页：'))
end=int(input('请输入结束页：'))
for i in range(start,end+1):
    pn=(start-1)*50
    url=f'{url}kw={name}&ie=utf-8&pn={pn}'
    html=urllib.request.urlopen(url)
    html_read=html.read().decode('utf-8')
    with open(f'{name1}的贴吧第{i}页.html', mode='w',encoding='utf-8')as f:
        print(f'正在写入第{i}页......')
        f.write(html_read)

