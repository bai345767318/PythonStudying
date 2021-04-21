'''
创建数组--   1.空的/随机
            2.零填充
            3. 1填充
'''

import numpy as np

#  1. numpy.empty
#   用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组

# 格式：numpy.empty(shape, dtype = float, order = 'C')     #empty:空的
# shape	数组形状
# dtype	数据类型，可选
# order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

x = np.empty([3, 2], dtype=int)  # 随机值
print(x)

#  2. numpy.zeros
# 创建指定大小的数组，数组元素以 0 来填充：
# 格式：numpy.zeros(shape, dtype = float, order = 'C')
# shape	数组形状
# dtype	数据类型，可选
# order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组

# 默认为浮点数
x = np.zeros(5)
print(x)
# 设置类型为整数
y = np.zeros((5,), dtype=np.int8)#此处需指定长度
print(y)
#自定义类型
z = np.zeros((2,2),dtype= [('x','i4'),('y','i4')])
print(z)

# 3.numpy.ones'
#创建指定形状的数组，数组元素以 1 来填充
# shape	数组形状
# dtype	数据类型，可选
# order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组

#默认为浮点数
x = np.ones(5)
print(x)
#自定义类型
x = np.ones([2,3],dtype=int)#此处无需指定长度
print(x)


print("**********note**********")
from numpy import *
#创建正态分布数组
#创建randn（size）俯冲X~N（0,1）的正态分布随机数组
a = random.randn(2,3)#dtype 默认浮点型
print(a)

#创建随机分布固定size及范围的整数型数组
#randint（[low,high],size）
a = random.randint(100,200,(3,3))
print(a)
#arange创建数组
a = np.arange(10)
b  = np.arange(10,20)
c =np.arange(10,20,2)
print(a)
print(b)
print(c)
#eye创建对角矩阵数据
a = np.eye(5)
print(a)

#order中的C是从低维度度开始读写，F反之
a = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
# a.shape(2,3,2)############有问题
# print(a)
n = np.reshape(a,(4,3)) #这里默认order为C
print(n)

m = np.reshape(a,(4,3),order='F')
print(m)


