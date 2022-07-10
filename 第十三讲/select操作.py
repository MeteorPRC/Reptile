from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
url='https://www.17sucai.com/pins/demo-show?id=42276&st=eODDJO5dH5bpgz_b2XNJ6Q&e=1656853133'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(2)
driver.switch_to.frame(driver.find_element(By.ID,'iframe'))
time.sleep(1)
SelectXpath=driver.find_element(By.XPATH,'//*[@id="selectDemo"]/xm-select/div[1]')
SelectXpath.click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="selectDemo"]/xm-select/div[3]/div/div[2]/div[1]/div').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="selectDemo"]/xm-select/div[3]/div/div[2]/div[3]/div').click()
time.sleep(1)
driver.close()
# RK=14fl/LwRYd; ptcz=196d284ef402cae79254e6ba19d4ee021fef2602594337a9f9ce008fc42bfa13; qz_screen=1536x864; pgv_pvid=6809229600; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; __Q_w_s_hat_seed=1; eas_sid=r1o675c6t580f8t4p9S6c9j2Z1; LW_uid=y1o6t5T639g4T2g8G159e3M683; LW_sid=J1J6p5z6g9R4Z2u8K2J0d4V8c8; _qpsvr_localtk=0.12825706205477805; pgv_info=ssid=s3156211072; uin=o1824783344; skey=@cqOjE860V; p_uin=o1824783344; pt4_token=WCpKAtuPMFamFSpmW8ij2IEX217AVp2qxKO4UQUoX5I_; p_skey=z7Hdfla0svNJj4mxd4W0e2xU0Nc-TtpNxPNSfAuaoXo_; Loading=Yes; scstat=6; 1824783344_todaycount=-2; 1824783344_totalcount=-2