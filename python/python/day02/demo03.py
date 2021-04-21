'''
集合 set
'''

# 集合中的元素不能重复
# 重复元素在set中自动过滤
# set没有顺序
classmates = ['毛磊','白金哲','曹皓天','程凯平','陈盼','程凯平']
print(classmates)
# 创建集合时，需要提供一个列表作为输入
s = set(classmates)
# {'毛磊', '曹皓天', '程凯平', '白金哲', '陈盼'}
print(s)

# 添加
s.add('白金哲')
print(s)
s.add('刘宵芬')
print(s)

# 删除
s.remove('白金哲')
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])

# 求交集
print(s1 & s2)
# 求并集
print(s1 | s2)