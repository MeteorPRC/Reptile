from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
需求: 对我们的爬虫书进行数据的爬取 拿到对应的价格/书名/评价数量/店铺或则出版社 
加另外一个课外的需求  将数据保存到csv文件中  

页面分析
通过分析发现我们要的数据都在ul中的li标签中 
每30个刷新一次 但是对于我们的selenium我们是不用去分析我们的数据接口的 
通过滑动滚轮获取单个页面中所有的数据 然后再去解析我们想要的数据 

思路分析:
1 先打开京东的网站
2 输入内容(爬虫书)
3 点击搜索按钮
4 把我们的滚轮拖到最下面
5 爬取单个页面中的数据 并通过解析获取我们想要的数据 
6 翻页处理 (先弄单个后面再弄多页 find去进行一个判断就ok了)

代码实现:
具体如下
'''


# 面向对象的编程思想进行实现
class JDspider:
    # 初始化属性
    def __init__(self):  # 在创建完对象后init方法会自动的去执行
        # 加载驱动
        self.driver = webdriver.Chrome()

        # 拿到目标url
        self.driver.get('https://www.jd.com/')

        # 定位到搜素框然后输入我们想要查找的内容
        input_tag = self.driver.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')

        # 延迟两秒
        time.sleep(2)

        # 定位搜索按钮 然后触发click事件
        button_tag = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        button_tag.click()

        # 延迟两秒
        time.sleep(2)

    # 解析数据的函数
    def Parse_html(self):
        # 把我们的滚轮拖到最下面  js代码 不需要同学们去记忆 但是可以去总结
        # 0 表示的是从起始位置开始 第二个参数代表的是整个窗口的高度
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )

        time.sleep(3)  # 强制等待三秒   页面等待 提高我们的selenium效率
        # 通过抓包定位到商品信息存在的ul与li标签上   li是存在多个的 elements
        lilist = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')

        # 遍历lilist 拿到每一个li 人再在li中获取我们想要的数据
        for li in lilist:
            # 定义一个字典 用于保存我想要的数据
            try:
                item = {}
                # strip() 默认去除空格
                item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]/strong').text.strip()
                item['book_name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
                item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
                item['shop_press'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]/a').text.strip()
                print(item)
            except Exception as e:
                print(e)

    '''
    写完上面的函数 发现只能获取单页的数据 但是需求是获取100的数据 那这个时候
    我们需要进行一个翻页的处理 
    处理翻页的解决方案: find  -1到最后一页
     下一页属性 1-99 pn-next    100 pn-next disabled 都获取成功了！！
    '''

    # 获取下一页方法
    def next_html(self):
        while True:  # 100次
            self.Parse_html()  # self代指我们当前的对象  100  100页找到pn-next disabled返回的是一段数字
            print("*" * 50)
            if self.driver.page_source.find('pn-next disabled') == -1: # 1-99页都成立
                next_tag = self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]')
                next_tag.click()
            else:
                self.driver.quit()
                break  # 退出死循环一定要写


if __name__ == '__main__':
    # 创建对象
    spider = JDspider()
    spider.next_html()
