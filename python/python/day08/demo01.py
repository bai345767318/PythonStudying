'''
网络爬虫 spider
'''

import requests
from lxml import etree


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

# 发出请求，并接收响应
response = requests.get('https://www.baidu.com/',headers=headers)
# 指定编码集
# print(response.encoding)
response.encoding = 'utf-8'
# 以文本的方式输出响应内容
# print(response.text)
# 以二进制的方式输出响应内容
print(response.content)

# 将文本转换为电子树结构
tree = etree.HTML(response.text)
# 在页面中抓取图片的地址
src = tree.xpath('//*[@id="s_lg_img"]/@src')

# 下载图片
response = requests.get('https:'+src[0],headers=headers)
with open('logo.png','wb') as file:
    file.write(response.content)


