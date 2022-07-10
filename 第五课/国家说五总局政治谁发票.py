import requests
'''
url不被信任
可以用verify=false 关闭ssl证书认证
其中verify=True是默认
'''
url='https://inv-veri.chinatax.gov.cn/'
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
response=requests.get(url,headers=header,verify=False)
print(response.text)