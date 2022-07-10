import requests

'''
https://video.pearvideo.com/mp4/short/20220415/cont-1758697-15862042-hd.mp4
https://video.pearvideo.com/mp4/short/20220415/1654589229347-15862042-hd.mp4
'''
url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1758697&mrd=0.00803084803401899'
# referer参数
re_url = 'https://www.pearvideo.com/video_1758697'
id = re_url.split("_")[1]
print(id)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Referer': re_url
}
# 获取响应对象
respones=requests.get(url,headers=headers)
# 检查是否向应成功
print(respones)

dic=respones.json()
print(dic,type(dic))
vurl=dic['videoInfo']['videos']['srcUrl']
print(vurl)
systemTime=dic['systemTime']
# print(systemTime)
result=vurl.replace(systemTime,f'cont-{id}')
# print(result)
re=requests.get(result)
with open('梨视频.mp4',mode='wb') as f:
    print('正在写入视频...')
    f.write(re.content)