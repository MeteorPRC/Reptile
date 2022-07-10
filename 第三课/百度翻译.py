import requests
import time

'''
通过百度翻译
'''
url = 'https://fanyi.baidu.com/sug'
kw = input('要翻译的内容：')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
data = {
    'kw': kw
}
response = requests.post(url, data=data, headers=headers)
html = response.json()
print(html['data'][0]['v'])

