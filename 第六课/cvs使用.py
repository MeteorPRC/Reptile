# import csv
#
# m = [
#     {'name': '找', 'age': 23, 'gender': '男'},
#     {'name': '找1', 'age': 23, 'gender': '男'},
#     {'name': '找2', 'age': 23, 'gender': '男'}
# ]
# headers=('name','age','gender')
# with open('练习acsv.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     #创建writer
#     writer=csv.DictWriter(f,headers)
#     # 写入表头（表头不会自己创建）
#     writer.writeheader()
#     # 写入内容
#     writer.writerows(m)


# import csv
#
# m = {
#     (1, 2, 3),
#     (12, 2, 3),
#     (123, 2, 3)
# }
# headers=('数字一','数字二','数字三')
# with open('练习二.csv', 'w', encoding='utf-8-sig',newline='') as f:
#     # 创建文件
#     writer=csv.writer(f)
#     # 写入内容
#     writer.writerows(m)

# 读取内容
import csv
with open('练习acsv.csv','r',encoding='utf-8-sig',newline='')as f:
    # 创建一个读对象
    reader=csv.DictReader(f)
    print(reader)
    for i in reader:
        print(i)
        for x,y in i.items():
            print(x,y)