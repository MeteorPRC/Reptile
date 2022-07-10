import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
url1='https://www.baidu.com/'
url2='https://search.jd.com/Search?keyword=python%E7%88%AC%E8%99%AB&enc=utf-8&pvid=2b806759184449d49ec7ebb426c4aaf2'
driver=webdriver.Chrome()
driver.get(url1)
driver.execute_script(f'window.open("{url2}")')
time.sleep(1)
print(driver.current_url)
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
print(driver.window_handles)
# 鼠标行为链
input_tag=driver.find_element(By.ID,'kw')
button_tag=driver.find_element(By.ID,'su')
actions=ActionChains(driver)  #  actions  行动
actions.send_keys_to_element(input_tag,'python')
time.sleep(3)
actions.perform()

# actions.move_to_element(button_tag)
time.sleep(3)

actions.click(button_tag)
# time.sleep(1)
actions.perform()
time.sleep(3)
# actions.click()
time.sleep(3)



