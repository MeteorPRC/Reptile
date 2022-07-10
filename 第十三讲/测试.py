# import time
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# # 这个是绝对路径
# driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver",
#                           options=options)
# driver.get("https://www.baidu.com/")
#
# # 最大化浏览器
# driver.maximize_window()
# time.sleep(3)
# driver.close()

# -*- coding = utf-8 -*-
# @Time : 2021/10/16 17:47
# @Author : LIUYU
# @File : test_selenium.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver")
driver = webdriver.Chrome(service=s)
driver.get('https://www.baidu.com')
driver.close()