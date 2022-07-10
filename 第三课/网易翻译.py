from urllib import request
from urllib import parse
import json
name=input('请输入你要翻译的内容；')
url='https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# print(parse.quote(name))
data={
    "i":name,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"16544348474166",
    "sign":"d7b85e6d0818797bfba5db5c31a1f377",
    "lts":"1654434847416",
    "bv":"f6814c1c974e0612ddcf7cf95130f445",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME"
}
explain=parse.urlencode(data)
#需要转换data为bytes格式，并设置编码格式为utf-8,不然调用data时会报错
data=bytes(explain,encoding='utf-8')
# print(explain)
package=request.Request(url,data=data)#包装
# print(package)
response=request.urlopen(package)
html=response.read().decode('utf-8')
# print(html,type(html))
html_jl=json.loads(html)
print(html_jl,type(html_jl))
print(html_jl['translateResult'][0][0]['tgt'])