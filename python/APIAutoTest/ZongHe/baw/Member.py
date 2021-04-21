'''
Member模块的接口
'''


def register(url, baserequests, data):
    '''
    注册
    :param url: 环境信息，比如 http://jy001:8081/
    :param baserequests:BaseRequests的实例
    :param date:注册的测试数据
    :return:响应信息
    '''
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url, data=data)
    return r


def list(url, baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r


def login(url, baserequests, data):
    '''
    登录
    :param url:
    :param baserequests:
    :param data:
    :return:
    '''
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url, data=data)
    return r


# 测试代码
if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests
    b = BaseRequests()

    canshu = {'mobilephone': "18011112222", "pwd": "123456"}
    r = register("http://jy001:8081/", b, canshu)
    print(r.text)
