import requests
import csv
from lxml import etree

'''
要求：
爬取懂车帝网页的动车排行榜：
车名（name）、车况（situation）、价格（price））

网址分析：
https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E4%BF%9D%E5%AE%9A&count=10&offset=10
https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E4%BF%9D%E5%AE%9A&count=10&offset=20&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0
https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E4%BF%9D%E5%AE%9A&count=10&offset=30&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0

'''


def source(url, i):  # 获取源码
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    if i == 0:
        html = response.content.decode()
    else:
        html = response.json()
    # print(html)
    return html


def transform(html):  # xpath处理转换
    element = etree.HTML(html)
    # print(html)
    carxpath = element.xpath("//ol/li[@class='list_item__3gOKl']")
    carlist = []
    # print(carxpath)
    for itme in carxpath:
        cardict = {}
        # 获取车名
        name = itme.xpath("./div[@class='tw-py-16 tw-pr-12']/div[@class='tw-leading-28 tw-h-28 tw-truncate']/a/text()")[
            0]
        # print(name)
        # 获取车型
        situation = itme.xpath(
            "./div[@class='tw-py-16 tw-pr-12']/div[@class='tw-leading-28 tw-h-28 tw-truncate']/span[@class='tw-text-12 tw-text-color-gray-700 tw-ml-6']/text()")[
            0]
        # print(situation)
        #  车辆价格
        price = itme.xpath("./div[@class='tw-py-16 tw-pr-12']/p/text()")[0]
        # print(price)
        # 详情
        details = \
        itme.xpath("./div[@class='tw-py-16 tw-pr-12']/div[@class='tw-leading-28 tw-h-28 tw-truncate']/a/@href")[0]
        # print(details)
        cardict["name"] = name
        cardict["situation"] = situation
        cardict['price'] = price
        cardict['url'] = f'https://www.dongchedi.com/{details}'
        # print(cardict['url'])
        carlist.append(cardict)
    # print(carlist)
    return carlist


def transform2(html):
    carlist = []
    for x in range(0, 10):
        cardict = {}
        name = html['data']['list'][x]['series_name']
        print(name)  # 车名
        # 获取车型
        situation = html['data']['list'][x]['sub_brand_name']
        print(situation)
        #  车辆价格
        price = html['data']['list'][x]['dealer_price']
        print(price)
        # 详情链接
        details = html['data']['list'][x]['series_id']
        # print()
        url = f'https://www.dongchedi.com//auto/series/{details}'
        print(url)
        cardict['name'] = name
        cardict['situation'] = situation
        cardict['price'] = price
        cardict['url'] = url
        carlist.append(cardict)
    return carlist


def save(carlist, i):  # 保存
    if i == 0:
        p = 'w'
    else:
        p = 'a'
    with open('汽车销量排行榜.csv', p, encoding='utf-8-sig', newline='') as f:
        if i == 0:
            writer = csv.DictWriter(f, fieldnames={'name', 'situation', 'price', 'url'})
            writer.writeheader()
        else:
            writer = csv.DictWriter(f, fieldnames={'name', 'situation', 'price', 'url'})
        writer.writerows(carlist)


if __name__ == '__main__':  # 程序主入口
    # for i in range(10,50,10):
    #     print(i,'-------------------------------------------------')
    #     url = f'https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E4%BF%9D%E5%AE%9A&count={i}&offset=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0'
    start = eval(input('请输入要查询几组（10个为一组）：'))
    i = 0
    while i < start and start < 8:
        if i == 0:
            url = 'https://www.dongchedi.com/sales'
            html = source(url, i)  # 源
            carlist = transform(html)
            save(carlist, i)
            i += 1
        else:
            url = f'https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E4%BF%9D%E5%AE%9A&count10&offset={i * 10}&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0'
            html = source(url, i)
            carlist = transform2(html)
            save(carlist, i)
            i += 1
