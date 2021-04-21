'''
自动管理Cookie
通过requests.session 自动管理Cookies
'''

import requests

s = requests.session()

#登录百格
print("=============登陆前的Cookies",s.cookies)
url = "https://www.bagevent.com/user/login"
user = {
    # "Cookie":'_ga=GA1.2.989794973.1606976726; MEIQIA_TRACK_ID=1l8RRfG8a6e48kfcB3vq2dEqnzR; __auc=d49f42201762746ea25ea318a79; __asc=1cb458451762cc022c0f1a39f03; _gid=GA1.2.1036987633.1607068579; MEIQIA_VISIT_ID=1lBUBMpvprYDc9OL0ygl8DFA30l; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1607068558,1607069840,1607070176,1607070265; BAGSESSIONID=b724ed99-fba2-472d-88da-ab687a057300; JSESSIONID=92DB1BA2BCA181799959F17D7C7B5526; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607071273'
    "access_type":"1",
    "loginType":"1",
    "emailLoginWay":"0",
    "account":"2780487875@qq.com",
    "password":"qq2780487875",
    "remindmeBox":"on",
    "remindme":"1"
}
r = s.post(url,data=user)
print(r.text)
print("================登陆后的Cookies",s.cookies)

#获取账户的信息
url="https://www.bagevent.com/account/dashboard"
r = s.get(url)
# print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

#退出登录
url ="https://www.bagevent.com/user/login"
r = s.get(url)
# print(r.text)
print("=============退出登陆后的Cookies",s.cookies)
#前后s.Cookies有一点点区别
