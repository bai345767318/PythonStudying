'''
Cookies:
http协议：无状态，无连接，媒体独立
每个请求都是独立的，有一些接口登录后才能访问，需要使用Cookies验证用户是否登录
account/dashborad 用户没有登录时，返回登录的页面
account/dashborad 如果登录了，返回的详细信息。浏览器登录后，获取到的cookies直接放到自动化来用。
如果cookies失效或者其他用户登录，就不能继续访问了。
'''
import requests

# 百格网站，有一些接口登录之后才能访问
print("未登录时，返回结果为：")
url="https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 用fiddler抓到的包，将里面的头设置到这里
head = {
    "Cookie":'_ga=GA1.2.989794973.1606976726; MEIQIA_TRACK_ID=1l8RRfG8a6e48kfcB3vq2dEqnzR; __auc=d49f42201762746ea25ea318a79; __asc=1cb458451762cc022c0f1a39f03; _gid=GA1.2.1036987633.1607068579; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; MEIQIA_VISIT_ID=1lBUBMpvprYDc9OL0ygl8DFA30l; JSESSIONID=8F965875514663B04B93DD479D72B387; BAGSESSIONID=bab2b710-d45b-48a2-906b-ee1545eb233b; _gat=1; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1607068558,1607069840,1607070176,1607070265; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607070265'
}

r = requests.get(url, headers=head)
print(r.text)

