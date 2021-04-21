'''小说版本2.0

下载所有玄幻小说 函数封装'''
'''小说版本1.2

下载每部小说，捕捉异常，函数封装'''
import requests
from lxml import etree


def c_downloader(title,url):
    try:
        #1.给服务器发送请求
        response=requests.get(url)
        response.encoding='utf-8'
        #将网页转为电子数结构
        tree=etree.HTML(response.text)
        #获取章节标题
        ctitle = tree.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')[0]
        print('正在下载：%s'%ctitle)
        #获取章节内容
        content=tree.xpath('//*[@id="content"]/text()')
        #解决内容中有字符串问题
        a = ''.join(content)

        #保存
        with open(title,'a',encoding='utf-8') as file:
            file.write(ctitle+a)
    except Exception as e:
            print(e)
            c_downloader(title,url)
            #当出现问题时，一直掉自己，直到成功为止就下一次

#下载指定小说，等下载后就去掉，下载内容函数
def downloader(url):

    #获取所有章节地址
    response = requests.get(url)
    response.encoding = 'utf-8'

    tree= etree.HTML(response.text)

    #获取所有章节列表
    links = tree.xpath('/html/body/div[5]/dl/dd/a/@href') 
    title = tree.xpath('/html/body/div[4]/div[2]/h2/text()')[0]
    print('正在下载小说...%s'%title)
    #完善章节地址
    links=[url+link for link in links]

    #开始下载所有章节
    for link in links[0:10]:
        c_downloader(title,link)
    
def downloader1(url):   
    #获取所有玄幻兄啊说地址

    #发送请求
    response = requests.get(url)
    tree = etree.HTML(response.text)
    #获取所有玄幻小说列表
    mikes = tree.xpath('/html/body/div[4]/div[2]/div/ul/li/span[2]/a/@href')
                        
    #开始下载所有玄幻小说
    for mike in mikes[0:3]:
        downloader(mike)
    
if __name__ =="__main__":
    urls =['http://www.shuquge.com/category/1_%d.html'%i for i in range(1,1338)]
    for url in urls[:4]:
        downloader1(url)




