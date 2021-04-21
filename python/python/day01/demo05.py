'''
列表 list
'''

# 列表中的每一个值称为元素-element
# 列表是有序的，列表的顺序也称为索引-index，从0开始

# 创建列表
#                0      1       2       3       4
classmates = ['毛磊','白金哲','曹皓天','程凯平','陈盼']
print(classmates)
print('列表长度=',len(classmates))

# 获取列表中指定的元素
name0 = classmates[0]  # 索引，也可以叫做下标
print(name0)
# print(classmates[5]) # list index out of range
print(classmates[len(classmates)-1]) # 访问列表最后一个元素
# 索引可以是负数，表示从后向前数
print(classmates[-1])

# 向列表中添加元素
# 添加到末尾
classmates.append('干钧')
print(classmates)
print(classmates[-1])

# 插入到中间
classmates.insert(2,'侯富君')
print(classmates)

# 删除元素
# 删除末尾元素并返回
name = classmates.pop()
print(name)
print(classmates)

# 删除指定下标的元素并返回
name = classmates.pop(3)
print(name)
print(classmates)

# 修改元素
classmates[0] = '刘厚祥'
print(classmates)

# 清除所有元素
# classmates.clear()
# print(classmates) # [] 空列表

# 获取指定元素的索引
print(classmates.index('程凯平'))


l = [1,2,3,4]
m = [True,False,False]
n = [1,'tom',True,None]

# [[1, 2, 3, 4], [True, False, False], [1, 'tom', True, None]]
o = [l,m,n]
print(o[2][1])
