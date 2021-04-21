'''
发送post请求
'''
import requests

# 登录接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "15127025702",
    "pwd": "123456"
}
# 用data传表单数据， "Content-Type": "application/x-www-form-urlencoded", 参数在form中
r = requests.post(url, data=user)
print(r.text)
print("********分隔线*********")
# 用data传表单数据
url = "http://httpbin.org/post"
user = {
    "mobilephone": "15127025702",
    "pwd": "123456"
}
r = requests.post(url, data=user)
print(r.text)
print("*******分隔线********")
# 用json传参数，"Content-Type": "application/json"  参数在json中

r = requests.post(url, json=user)
print(r.text)

# 练习：充值接口，给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone": "15127025702",
    "amount": 99512.5
}
r = requests.post(url, data=user)  # 使用date还是json传参，要看接口实现的是哪个
print(r.text)

# r = requests.post(url,json=user)#json 失败
# print(r.text)#{"status":0,"code":"20103","data":null,"msg":"手机号不能为空"}

# 取现
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/withdraw"
user = {
    "mobilephone": "15127025702",
    "amount": 300000
}
r = requests.post(url, data=user)
print(r.text)
