import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url='https://www.douban.com/'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="anony-reg-new"]/div/div[1]/iframe'))
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(1)
driver.find_element(By.ID,'username').send_keys('123456789')
time.sleep(1)
driver.find_element(By.ID,'password').send_keys('987654321')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(1)
driver.save_screenshot('豆瓣登录.png')
time.sleep(1)
driver.quit()

