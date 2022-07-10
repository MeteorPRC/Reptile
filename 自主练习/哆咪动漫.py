import requests
import re
import csv
from fake_useragent import UserAgent


ua=UserAgent().chrome
# print(ua)
header={
    'user-agent':ua
}
url='https://www.dmdm2020.com/dongmantype/20.html'
response=requests.get(url,headers=header)
html=response.content.decode('utf-8')
print(html)