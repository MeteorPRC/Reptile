import requests
import json
from urllib import parse
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-06-10&leftTicketDTO.from_station=TSP&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Cookie': '_uab_collina=165459015529822403567779; JSESSIONID=113F6DA0B8F87CDB1117C581033CD137; RAIL_EXPIRATION=1654895243722; RAIL_DEVICEID=bIeaEZQIU3qF9-VTwDjHP5Jm5LDTaQCBKbf41jFM9VwUbaWbHoIRtRDCI2TDWe9ZyR9XrM0OLm8vOIMPA5kp6HW2ErrvzdewRMXjYnt3ZoljU0nZ3ozp7i2DPROXVmgnjbvKpjLT5Amignq5AFOk5HXf9Tor_2eY; highContrastMode=defaltMode; guidesStatus=off; cursorStatus=off; _jc_save_wfdc_flag=dc; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_toDate=2022-06-09; BIGipServerpassport=954728714.50215.0000; BIGipServerpool_passport=182714890.50215.0000; _jc_save_fromStation=%u5510%u5C71%2CTSP; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2022-06-10; BIGipServerotn=368050698.24610.0000'
}
res=requests.get(url,headers=header)
# print(res.content.decode('utf-8'))
data=res.json()
print(data['data']['result'])
print('---------------')
for i in data['data']['result']:
    print(i)
    print('---------------------')
    # count=0
    temp_list=i.split('|')
    # print(temp_list)
    # 计数
    # for j in temp_list:
    #     # print(count,j)
    #     count+=1
    if temp_list[3]!='无' and temp_list[31]!='':
        print(f'{temp_list[3]} 有票 一等座剩余： {temp_list[31]}')
    else:
        print(temp_list[3],'无票')

"""
车次 count=3
出发时间 count=8
商务座特等座 count=32
一等座 count=31
二等座\\二等包座 count=30

"""