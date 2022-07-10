import requests
url='http://www.chinatax.gov.cn/'
response=requests.get(url)
html=response.content.decode('utf-8')
print(html)