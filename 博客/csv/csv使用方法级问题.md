### python写入csv 用Excel打开乱码的解决方法

* 设置编码格式为utf-8-sig即可解决

### 写入后的文件内容回每行都会隔一行空行 
* 在文件吸入人的时候加上newline=''即可：
    ```python
    with open('练习csv.csv','w',encoding='utf-8-sig',newline='') as f:
    ```
