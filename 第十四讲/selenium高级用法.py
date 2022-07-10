import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver= webdriver.Chrome()
driver.get('https://www.baidu.com/')
html=driver.page_source
print(html )