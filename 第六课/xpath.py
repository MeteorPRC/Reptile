from lxml import etree
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """
# 将html文件转换成xml文件   etree.html,将字符串转化为Element
element=etree.HTML(wb_data)
print(type(element))
html=element.xpath('//div//ul//li//a//text()')
print(html)
html1=element.xpath('//div//ul//li[3]//@href')
print(html1)