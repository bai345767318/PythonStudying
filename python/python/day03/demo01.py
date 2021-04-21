'''
Python高级特性
'''

l = [1,2,3,4,5,6,7,8,9]
m = [l[0],l[1],l[2],l[3]]
print(m)

n = []
for i in l:
    if l.index(i)<4:
        n.append(i)
print(n)

'''
切片 l[start:end:step]
'''

l = [1,2,3,4,5,6,7,8,9]
m = l[0:4]
print(m)
print(l[4:7])

# 索引从0开始时可以省略
print(l[:4:1])
print(l[5:])
print(l[-3:])
print(l[:-3])

# 步长
print(l[::2])
print(l[1::2])
print(l[2::3])

# 元组也可以使用切片
t = tuple(range(100))
# print(t)
print(t[::5])

# 字符串也可以使用切片
s = 'abcdefg'
print(s[::2])