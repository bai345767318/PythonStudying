'''
测试前置和后置
'''
#类级别和方法级别。
#类级和方法级配合使用。
class Test001:
    def setup_class(self):#名字不能写错
        print("测试前置：class级别的，类开始执行一次")
    def teardown_class(self):#名字不能写错
        print("测试后置：class级别，类结束后执行一次")
    def setup_method(self):#名字不能写错
        print("测试前置：method级别的")
    def teardown_method(self):#名字不能写错
        print("测试后置：method级别的")

    def test_001(self):
        print("测试脚本1")
    def test_002(self):
        print("测试脚本2")
    def test_003(self):
        print("测试脚本3")
