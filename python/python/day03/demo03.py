'''
列表生成式 List Comprehensions
'''

l = [1,2,3,4,5]
# 利用range(start,end,step)函数生成列表
m = list(range(10))
print(l)
print(m)
n = list(range(0,10,2))
print(n)
# [0, 2, 4, 6, 8]
# [0, 4, 16, 36, 64]
o = []
n = list(range(0,10,2))
for x in n:
    o.append(x*x)
print(o)

# 列表生成式
p = [x*x for x in n]
print(p)

# 可以添加条件
q = [x*x for x in range(10) if x%2==0]
print(q)

# 可以使用双重循环
r = [x+y for x in 'ABC' for y in 'XYZ']
print(r)


import os
# s = [d for d in os.listdir(r'D:\workspace\python\day03')]
s = [d for d in os.listdir(r'c:')]
print(s)