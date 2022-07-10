import requests
'''
下载梨视频
https://video.pearvideo.com/mp4/short/20220415/cont-1758757-15862333-hd.mp4
'''
url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1758757&mrd=0.04864797585848035'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Referer': 'https://www.pearvideo.com/video_1758757'
}
response = requests.get(url, headers=header)
html = response.json()
systemTime=html["systemTime"]
srcurl=html["videoInfo"]["videos"]["srcUrl"]
id=header['Referer'].split('_')[1]
# print(id)
cont=f'cont-{id}'
url1=srcurl.replace(systemTime,cont)
print(url1)

'''
print(html, type(html))

html = {
    "resultCode": "1",
    "resultMsg": "success", "reqId": "cc57784e-bce9-499e-a2f9-0a4a829c2795",
    "systemTime": "1655101256169",
    "videoInfo": {"playSta": "1", "video_image": "https://image.pearvideo.com/cont/20220415/cont-1758757-12668262.png",
                  "videos": {"hdUrl": "", "hdflvUrl": "", "sdUrl": "", "sdflvUrl": "",
                             "srcUrl": "https://video.pearvideo.com/mp4/short/20220415/1655101256169-15862333-hd.mp4"}}
}
'''

