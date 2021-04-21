'''
数组属性
'''
#秩：轴（axis）的数量、维度（dimensions）
# axis = 0 表示沿着第0轴进行操作，axis = 1 表示沿着第1轴进行操作

#ndarray的属性有：
# ndarray.ndim	秩，即轴的数量或维度的数量
# ndarray.shape	数组的维度，对于矩阵，n 行 m 列
# ndarray.size	数组元素的总个数，相当于 .shape 中 n*m 的值
# ndarray.dtype	ndarray 对象的元素类型
# ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
# ndarray.flags	ndarray 对象的内存信息
# ndarray.real	ndarray元素的实部
# ndarray.imag	ndarray 元素的虚部
# ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

import numpy as np

a = np.arange(24) #a现在只有一个维度 arange（范围）
print(a.ndim)
b = a.reshape(2,4,3)#b现在有3个维度
# (2,4,5)则报错ValueError: cannot reshape（重塑） array of size 24 into shape (2,4,5)，不能对b再进行reshape
print(b.ndim)

print(a.shape)
print(a.reshape)
a = np.array([[1,2,3],[4,5,6]])
print(a.ndim)#返回其维度（列数）或者叫秩
print(a.shape)#以元组形式返回数组的行数和列数
#调整数组大小
a.shape = (3,2)
print(a)
#也可以用reshape
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
#c = a.reshape(3,4)  #不会对其进行0填充，会报错
print(b)

x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)# 以字节形式返回数组中每一个元素的大小(n/8)
y = np.array([1,2,3,4,5,6],dtype=np.float64)
print(y.itemsize)

#   ndarray.flags
# C_CONTIGUOUS (C)	数据是在一个单一的C风格的连续段中
# F_CONTIGUOUS (F)	数据是在一个单一的Fortran风格的连续段中
# OWNDATA (O)	数组拥有它所使用的内存或从另一个对象中借用它
# WRITEABLE (W)	数据区域可以被写入，将该值设置为 False，则数据为只读
# ALIGNED (A)	数据和所有元素都适当地对齐到硬件上
# UPDATEIFCOPY (U)	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
x = np.array([1,2,3,4,5])
print(x.flags)#显示内存信息
print(x.flat)#内存地址


# note
print("**********note**********")
a = np.array([[1,2,3],[4,5,6]])
print(a)

b = a.reshape((6,))
print(b)

# b = a.reshape(6)
# print(b)

b[0] = 100
print(b)

print(a)
