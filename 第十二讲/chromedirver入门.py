from selenium import webdriver
import time
# 安装
#  pip install selenium
# 组合
# selenium+phantomjs 无头浏览器 不用安装驱动
# selenium+chrome+驱动


driver = webdriver.Chrome()  # 驱动的目录
url='https://www.baidu.com/'
driver.get(url)
# driver.maximize_window()
# print(driver.get_window_size())
# driver.set_window_size(2000,2200)
# print(driver.get_window_size())
# print(driver.get_window_position())
# driver.close()
time.sleep(2)
driver.refresh()
driver.get('12306')