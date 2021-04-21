'''
迭代 Iteration
'''

l = [1,2,3,4,5,6,7,8,9]

# 迭代 - 通过循环遍历列表或元组
for i in range(5): # 可迭代对象
    print(i)

for s in 'abcdef': # 可迭代对象
    print(s)

# 字典也是可迭代对象
d = {'a':1,'b':2,'c':3}
# 迭代key
for k in d:
    print(k,':',d[k])

# 同时迭代key和value
for k,v in d.items():
    print(k,":",v)

# 迭代value
for v in d.values():
    print(v)

# 如何判断一个对象是可迭代对象？--字符串、列表、集合、字典,                  int不能迭代
from collections.abc import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(d,Iterable))
print(isinstance(set([1,2,3]),Iterable))
print(isinstance(1,Iterable))

# 在迭代时获取迭代索引以及元素
l = [1,2,3,4,5,6,7,8,9]
for i,v in enumerate(l):
    print(i,':',v)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)
