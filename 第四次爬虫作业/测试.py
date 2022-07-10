import requests
import re

url='https://music.163.com/#/discover/toplist?id=19723756'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
response=requests.get(url,headers=headers)
response.encoding='utf-8'
html=response.text
print(html)

result=re.match(r'.*?(<tbody>.*?</tbody>).*? ',html,re.S)
ul_content=result.group(1)
print(ul_content,len(ul_content))