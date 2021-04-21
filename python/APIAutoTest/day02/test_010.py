'''
mark标记
1.跳过用例，某个版本有缺陷，导致脚本执行不通过，可以跳过该用例，待缺陷解决后再继续执行。
2.脚本越来越多，如果想执行其中一部分脚本怎么班？使用自定义标记
    全量脚本，挑选了一部分作为冒烟测试的脚本，只想执行冒烟这部分的脚本。

'''

import pytest


@pytest.mark.smoke  # smoke、api:自定义标记
@pytest.mark.api
def test_001():
    print("测试用例1")


# 区别于   @pytest.mark.usefixtures("login")
@pytest.mark.skip("跳过的原因：尚未支持的功能，暂不执行，待实现后再执行")
def test_002():
    print("测试用例2")


def test_003():
    print("测试用例3")


@pytest.mark.api
def test_004():
    print("测试用例4")


class TestMark:
    def test_011(self):
        print("测试用例11")

    @pytest.mark.smoke
    def test_012(self):
        print("测试用例12")

    def test_013(self):
        print("测试用例13")

    @pytest.mark.api
    def test_014(self):
        print("测试用例14")


'''
-m="smoke or api" 配置文件
; -m=smoke 执行smoke标记的用例
; -m="smoke and api"  执行既有smoke又有api标记的用例
; -m="smoke or api"  执行有smoke或者api标记的用例
; -m="not smoke"  执行非smoke标记的用例
'''
