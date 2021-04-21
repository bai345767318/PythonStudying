#练习：
import pytest
import requests

@pytest.fixture(params=[
                        {"data":{"pwd":"1234567891234567891"},"except":{"msg":"手机号不能为空","code":"20103"}},
                        {"data":{"Mobilephone":"13454785815","pwd":"12345","rename":"曹贼"},"except":{"msg":"密码长度必须为6~18","code":"20108"}},
                        {"data":{"Mobilephone":"13156782375","pwd":"1234567891234567891","rename":"曹贼"},"except":{"msg":"密码长度必须为6~18","code":"20108"}},
                        {"data":{"Mobilephone":"131567","pwd":"123456123456123456","rename":"曹贼"},"except":{"msg":"手机号码格式不正确","code":"20109"}},
                        {"data":{"Mobilephone":"13454785815","pwd":"123456","rename":"曹贼"},"except":{"msg":"手机号码已被注册","code":"20110"}},
                        ])

def register_data(request):  # 参数request是固定的，不能写成其他
    return request.param  # 使用request.param返回每组数据
def test_register(register_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    print("测试数据",register_data['data'])
    print("预期结果",register_data['except'])
    r = requests.post(url,params=register_data['data'])
    print(r.text)
    # print(r.json())
    assert r.json()['msg'] == register_data['except']['msg']
    assert r.json()['code'] == register_data['except']['code']

