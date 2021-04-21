'''
字典 dict
使用key-value(键值对)的形式存储数据，查找速度特别快
'''

classmates = ['毛磊','白金哲','曹皓天','程凯平','陈盼']
scores = [80,90,77,93,88]

index = classmates.index('程凯平')
score = scores[index]
print('score=%d'%score)

# 声明一个字典 key:value
# 字典是无序的
# key的值是唯一的
# value的值不唯一
d = {'毛磊':80,'白金哲':90,'曹皓天':77,'程凯平':93,'陈盼':88}

# 查找 通过key找value
print(d['程凯平'])

# print(d['王薪宇']) # KeyError
# get()方法不会抛异常，如果没有则返回None
print(d.get('王薪宇'))

if '王薪宇' in d:
    print(d['王薪宇']) # KeyError

print('王薪宇' in d)
print('程凯平' in d)
# 添加
d['梁苗苗'] = 95
print(d)

# 修改
d['程凯平'] = 88
print(d)

# 删除
r = d.pop('程凯平')
print(r)
print(d)



