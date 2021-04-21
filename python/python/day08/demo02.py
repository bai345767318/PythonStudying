from lxml import etree

htm = '''<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
        <li class="item-0">else item</li>
    </ul>
</div>'''

tree = etree.HTML(htm)

# xpath语法
# 获取元素的文本

text = tree.xpath('//div/ul/li[2]/a/text()')
print(text)
# 获取元素属性的值
href = tree.xpath('//div/ul/li[2]/a/@href')
print(href)
href = tree.xpath('//div/ul/li/a/@href')
print(href)

# *: 通配符，表示任意元素
li_text = tree.xpath('//*[@class="item-inactive"]/a/text()')[0]
print(li_text)

li_text = tree.xpath('//div/ul/li[@class="item-inactive"]/a/text()')
print(li_text)