'''
小说下载器 
@VERSION 1.0
@AUTHOR Eric
'''

import requests
from lxml import etree

'''章节下载器'''
def c_downloader(url):
    try:
        # 获取小说章节页面
        response = requests.get(url)
        # 设定编码集
        response.encoding = 'utf-8'
        # 将网页text转换为DOM树
        tree = etree.HTML(response.text)
        # 获取章节标题
        title = tree.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')[0]
        print('正在下载%s...'%title)
        # 获取章节内容
        # content = tree.xpath('string(//*[@id="content"])')
        # print(''.join(content))
        content = tree.xpath('//*[@id="content"]/text()')
        result = ''
        for line in content:
            if line != '\r':
                result += line
        
        with open('剑来','a',encoding='utf-8') as file:
            file.write(title+result)
    except Exception as e:
        print(e)
        c_downloader(url)

# 下载指定的小说
def downloader(url):
    # 获取小说章节列表页面
    response = requests.get(url)
    tree = etree.HTML(response.text)
    # 获取所有的章节地址
    links = tree.xpath('/html/body/div[5]/dl/dd/a/@href')
    # 完善章节地址
    links = [url+link for link in links]
    # 开始下载所有章节
    for link in links:
        c_downloader(link)

if __name__ == "__main__":
    # 小说地址
    url = 'http://www.shuquge.com/txt/8659/'
    downloader(url)