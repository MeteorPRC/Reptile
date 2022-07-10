from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url='https://www.baidu.com/'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('csdn')
time.sleep(2)

driver.find_element(By.ID,'su').click()
time.sleep(2)
driver.save_screenshot('百度.png')
time.sleep(2)
driver.close()
driver.quit()
