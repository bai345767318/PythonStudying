'''
元组 tuple
'''

# 元组和列表非常相似，但是元组一旦创建，就不允许修改
classmates = ('毛磊','白金哲','曹皓天','程凯平','陈盼')
print(classmates)

# 根据索引获取元素
print(classmates[2])

# 声明只有一个元素的元组
t = (1,)
print(t)
m = ()
print(m)

# 强制转换为列表
n = list(classmates)
print(n)
# 强制转换为元组
p = tuple(n)
print(p)

# 元组中的数据真的不能改变吗？
t = (1,2,['a','b'])