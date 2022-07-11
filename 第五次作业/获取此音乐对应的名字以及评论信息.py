"""

提交日期：2022-7-11
提交人：18期爬虫-05-selenium作业-赵**

"""
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

'''
https://music.163.com/#/song?id=399354373
目标：评论者的网名，与评论
需要切换iframe
页面下拉
鼠标行为连点击下一页
'''


class WYYmusic:  # 音乐
    # 初始化类
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.get('https://music.163.com/#/song?id=399354373')  # 打开链接
        self.driver.implicitly_wait(3)
        self.driver.switch_to.frame(self.driver.find_element(By.ID, 'g_iframe'))
    # 操作
    def operate(self):
        # 歌评论
        for self.i in range(10):
            self.SongReview = []
            divlist = self.driver.find_elements(By.XPATH, '//*[@class="itm"]/div[2]')
            # print(divlist)
            for item in divlist:
                # print(i)
                # 评论
                try:
                    commentdict = {}
                    comment = item.find_element(By.XPATH, './/div[@class="cnt f-brk"]').text
                    name = comment.split("：")
                    commentdict['name'] = name[0]
                    commentdict['comment'] = name[1]
                    self.SongReview.append(commentdict)
                    # print(comment)
                    # print(name)
                except Exception as e:
                    print()
            self.save()
            # print(SongReview)
            #定位下一页按钮
            button_tag=self.driver.find_element(By.XPATH,'//*[@class="m-cmmt"]/div[3]/div/a[11]')
            action=ActionChains(self.driver)
            action.move_to_element(button_tag)
            action.click()
            action.perform()
        self.driver.quit()

    def save(self):
        if self.i == 0:
            self.mod='w'
        else:
            self.mod="a"
        headers=['name','comment']
        with open('评论.csv',self.mod,encoding='utf-8-sig',newline='')as f:
            writers=csv.DictWriter(f,headers)
            if self.i==0:
                writers.writeheader()
            writers.writerows(self.SongReview)

# 程序主入口
if __name__ == "__main__":
    # 爬虫
    reptile = WYYmusic()
    reptile.operate()
