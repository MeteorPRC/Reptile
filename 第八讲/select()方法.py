# # from bs4 import BeautifulSoup
# #
# # html_doc = """
# # <html><head><title>The Dormouse's story</title></head>
# # <body>
# # <p class="title"><b>The Dormouse's story</b></p>
# #
# # <p class="story">Once upon a time there were three little sisters; and their names were
# # <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# # <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# # <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# # and they lived at the bottom of a well.</p>
# #
# # <p class="story">...</p>
# # """
# # soup = BeautifulSoup(html_doc, 'lxml')
# # # 获取所有的tr标签
# # print(soup.select('#link2'))
# # print(soup.select('.story'))
# from bs4 import BeautifulSoup
# html = """
# <table class="tablelist" cellpadding="0" cellspacing="0">
#     <tbody>
#         <tr class="h">
#             <td class="l" width="374">职位名称</td>
#             <td>职位类别</td>
#             <td>人数</td>
#             <td>地点</td>
#             <td>发布时间</td>
#         </tr>
#         <tr class="even">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-25</td>
#         </tr>
#         <tr class="odd">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
#             <td>技术类</td>
#             <td>2</td>
#             <td>深圳</td>
#             <td>2017-11-25</td>
#         </tr>
#         <tr class="even">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>2</td>
#             <td>深圳</td>
#             <td>2017-11-25</td>
#         </tr>
#         <tr class="odd">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-25</td>
#         </tr>
#         <tr class="even">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-24</td>
#         </tr>
#         <tr class="odd">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-24</td>
#         </tr>
#         <tr class="even">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>4</td>
#             <td>深圳</td>
#             <td>2017-11-24</td>
#         </tr>
#         <tr class="odd">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-24</td>
#         </tr>
#         <tr class="even">
#             <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-24</td>
#         </tr>
#         <tr class="odd">
#             <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
#             <td>技术类</td>
#             <td>1</td>
#             <td>深圳</td>
#             <td>2017-11-24</td>
#         </tr>
#     </tbody>
# </table>
# """
# soup = BeautifulSoup(html,'lxml')
# # trs=soup.select('tr')[1:]
# # print(trs)
# # for i in trs:
# #     print(i)
# tr=soup.select('a')
# print(tr)
# for i in tr:
#     href=i.get('href')
#     print(href)
i = int(input(':'))
if i==1:
    print('-')
else:
    print('5')