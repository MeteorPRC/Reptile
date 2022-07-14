"""
项目：获取北京新发地产品价格
制作人：才短思涩-求解
制作时间：2022/7/12
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
'''
获取北京新发地的指定产品价格价
输入指定时间
获取时间选择框
'''
class XFD:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.xinfadi.com.cn/priceDetail.html')

        self.driver.implicitly_wait(120)
    # 时间选择模块    默认为当前时间日期
   '''
   时间模块太复杂，本人有点懒，先不写了
    def date(self):
        actions=ActionChains(self.driver)
        # 选择起始时间
        self.start_time=self.driver.find_element(By.ID,'demo19')
        # 选择结束时间
        self.end_time=self.driver.find_element(By.ID,'demo20')

        # 鼠标链点击事件起始时间

        actions.move_to_element(self.start_time)

        actions.click()
        actions.perform()
        actions.move_to_element()
    '''
    # 选择商品产品
    def product(self):
        


    # 操作模块
    def operate(self):
        pass


    # 信息保存模块
    def save(self):
        pass



if __name__=="__main__":
    # 选择
    choose=XFD()