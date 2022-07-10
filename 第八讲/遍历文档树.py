html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'lxml')
r1=soup.html.strings
# print(r1)
# for i in r1:
    # print(i)
r2=soup.html.stripped_strings
# print(r2)
# for i in r2:
    # print(i)

# x1=soup.find('a')
# print(x1)
# x2=soup.find_all('a')
# print(x2)
# x3=soup.find(['a','title'])
# print(x3)
x4=soup.find_all('a',attrs={'class':"sister",'id':"link1"})
print(x4)
for i in x4:
    print(i)