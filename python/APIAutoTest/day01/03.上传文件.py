'''
接口的功能是上传文件，比如上传头像，附加等
'''
import requests

url = "http://httpbin.org/post"
# 将本地的文件上传到服务器上
file1 = "d:/test.txt"
file1 = "d:\\test.txt"
file1 = r"d:\test.txt"
with open(file1, encoding='UTF-8', mode='r') as f:
    # 字典，上传的文件：文件相关参数组成的元组
    # text/plain 是文件的类型
    load = {
        "file1": (file1, f, "text/plain")
    }
    r = requests.post(url, files=load)
    print(r.text)
print("*************")
# 上传图片
file2 = "d:/001.jpg"
with open(file2, mode='rb') as f:
    load = {
        # 文件名：file-tuple
        # file-tuple 可以是二元组，三元组，四元组
        # image/jpg MIME类型，文件类型,application/json application/。。
        "file2": (file2, f, "image/jpg")
    }
    r = requests.post(url, files=load)
    print(r.text)

# 可以一次上传多个文件,文本和图片一起上传
with open(file1, encoding='UTF-8', mode='r') as f1:
    with open(file2, mode='rb') as f2:
        load = {
            "file1": (file1, f1, "text/plain"),
            "file2": (file2, f2, "image/jpg")
        }
        r = requests.post(url, files=load)
        print(r.text)
