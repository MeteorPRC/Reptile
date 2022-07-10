import requests
r = requests.get('https://www.baidu.com/')
#响应内容（str类型）
print('1r.text',type(r.text),r.text)
#响应内容（bytes类型）
print('2r.content',type(r.content),r.content)
#状态码
print('3r.status_code',type(r.status_code),r.status_code)
#响应头
print('4r.headers',type(r.headers),r.headers)
#Cookies
print('5r.cookies',type(r.cookies),r.cookies)
#URL
print('6r.url',type(r.url),r.url)
#请求历史
print('7r.history',type(r.history),r.history)
