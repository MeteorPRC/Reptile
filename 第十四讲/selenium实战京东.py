import time
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
需求：

爬取python爬虫书籍的数据进行爬取，拿到对应的价格、书名、评价数量、店铺或者出版社
"""


class JDspider:
    # 初始化属性
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.jd.com/')
        # 定位到输入框然后输入想要查找的内容
        input_tag = self.driver.find_element(By.XPATH, '//*[@id="key"]').send_keys('python爬虫')
        # 延迟两秒
        time.sleep(2)
        # 定位搜索按钮
        button_tag = self.driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
        button_tag.click()

    # 解析数据的函数
    def Parse_html(self):
        # 把我们的滚轮拖到最下面 js代码   不需要记忆 但是可以去总结
        # self.driver.execute_script(
        #     'window.scrollTo(0,document.body.scrollHeight)'
        # )
        time.sleep(3)
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)
        # 通过抓包获取定位的商品信息存在的ul与li
        lilist = self.driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')

        # 便利lilist 拿到每一个li 再让li中获取我们想要的数据
        for li in lilist:
            # print(li)
            try:
                item = {}
                item['price'] = li.find_element(By.XPATH, './/div[@class="p-price"]/strong').text.strip()
                item['book_name'] = li.find_element(By.XPATH, './/div[@class="p-name"]/a/em').text.strip()
                item['comment'] = li.find_element(By.XPATH, './/div[@class="p-commit"]/strong').text.strip()
                item['shop_press'] = li.find_element(By.XPATH, './/div[@class="p-shopnum"]/a').text.strip()
                print(item)
            except Exception as e:
                print(e)


    def next_html(self):
        a=1
        while True:
            self.Parse_html()
            print('*'*50)
            if self.driver.page_source.find('pn-next disabled') == -1 and a!=3:
                next_tag=self.driver.find_element(By.XPATH,'//*[@id="J_bottomPage"]/span[1]/a[9]')
                next_tag.click()
                a+=1
            else:
                self.driver.quit()
                break


if __name__ == '__main__':
    # 创建对象
    spider = JDspider()
    spider.next_html()
