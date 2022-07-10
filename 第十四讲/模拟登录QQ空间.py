import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import json
import re
# 加载驱动
driver=webdriver.Chrome()
# 目标url
url='https://qzone.qq.com/'
driver.get(url)
driver.switch_to.frame(driver.find_element(By.ID,'login_frame'))
time.sleep(1)
driver.find_element(By.ID,'img_out_1824783344').click()
time.sleep(2)
cookie=driver.get_cookies()
# print(cookie,type(cookie))
# for i in cookie:
#     print(i)
#     print('----------------')
cookie=[itme['name']+'='+itme['name'] for itme in cookie]
print(cookie)
cookie_str='; '.join(itme for itme in cookie)
print(cookie_str)
ua=UserAgent()
header={
    'user-agent':ua.chrome,
    'cookie':cookie_str
}
response=requests.get(url,headers=header)
html=response.content.decode('utf-8')
with open('QQ空间.html','w',encoding='utf-8')as f:
    f.writelines(html)

'''
RK=14fl/LwRYd; ptcz=196d284ef402cae79254e6ba19d4ee021fef2602594337a9f9ce008fc42bfa13; qz_screen=1536x864; pgv_pvid=6809229600; QZ_FE_WEBP_SUPPORT=1; __Q_w_s_hat_seed=1; eas_sid=r1o675c6t580f8t4p9S6c9j2Z1; LW_uid=y1o6t5T639g4T2g8G159e3M683; LW_sid=J1J6p5z6g9R4Z2u8K2J0d4V8c8; Loading=Yes; scstat=6; __Q_w_s__QZN_TodoMsgCnt=1; zzpaneluin=; zzpanelkey=; _qpsvr_localtk=0.5977226731764784; 1824783344_todaycount=0; 1824783344_totalcount=5818; pgv_info=ssid=s7774570999; uin=o1824783344; skey=@gbaPhtqf8; p_uin=o1824783344; pt4_token=ZanLmJv3DgVhsd2ZO4*BX*DCFvg8hgc5LaU7-JNZa68_; p_skey=PCHAd6U9AAJjPWqMUnDYT8p1h1BFVBpI9wHa4BXiXp4_; cpu_performance_v8=15
pragma: no-cache
'''