'''循环'''

r = 1+2+3+4+5+6+7+8+9+10
print(r)

'''for 循环'''
l = [1,2,3,4,5,6,7,8,9,10]
s = 0
# 求和
for i in [1,2,3,4,5,6,7,8,9,10]:
    '''
    1  i=1  s=1
    2  i=2  s=3
    ...
    10 i=10 s=55
    '''
    s = s+i

print('s=%d'%s)

# 1-1000
# 可迭代对象
s = 0
for i in range(101):
    s += i
print('s=%d'%s)

'''while 循环'''

# 100以内的所有的偶数的和

s = 0
n = 0
while n<=100: # 表达式的结果为True时执行循环语句，否则结束循环
    s += n
    n += 2
print(s)

# 当n>30时停止循环
# break 结束整个循环
n = 1
while n<=100:
    if n>30:
        break # 终止循环
    print(n)
    n += 1

# continue 结束本次循环
# 100以内的所有的偶数的和
s = 0
for i in range(101):
    # if i%2==0:
    #     s += i
    if i%2!=0: # 是奇数
        continue # 继续
    s += i

print('s=%d'%s)

# 死循环
# s = 0
# while True:
#     print(s)
#     s += 1

# 能否用for实现死循环?