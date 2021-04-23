# NumPy 官网 http://www.numpy.org/
# NumPy 源代码：https://github.com/numpy/numpy
# SciPy 官网：https://www.scipy.org/
# SciPy 源代码：https://github.com/scipy/scipy
# Matplotlib 官网：https://matplotlib.org/
# Matplotlib 源代码：https://github.com/matplotlib/matplotlib


import numpy as np

'''
格式： numpy.array(object,dtype = None,copy = True,order = None, subok = False,ndmin = 0)
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）在计算机内存中的存储元素的优先顺序
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
'''

a = np.array([1, 2, 3])
print(a)
# 多于一个维度
a = np.array([[1, 2], [3, 4]])
print(a)
# 最小维度
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
# dtype 参数
a = np.array([1, 2, 3], dtype=complex)
print(a)
