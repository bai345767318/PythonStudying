# 1. 实现一个trim()函数，利用切片取出字符串前后的空格
#    ' tom  '

# def trim(str1):
#     a = 0
#     li=list(str1)
#     for i in range(len(str1)):
#         while a <=(i+1):
#             if li[a:(a+1)] == ' ':
#                 li = li.pop[a:(a+1)]
#                 a +=1
#     return l
# print(trim([' tom ',' ',' '])
# li = ['a','d2','e3','4']
# # l1 = li.pop[0:2]
# print(li[0:2])
def trim(s):
    length = len(s)
    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break
        j = length-1
        while s[j] == ' ' and j >= i:
            j -= 1
        s = s[i:j+1]

    return s
print(trim(' tom '))



# 2. 随机生成一个5位的验证码，包含A-Za-z0-9
l = ['A','B','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z,''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
import random
p = [random.choice(l) for i in range(0,5)]
print(p)

# 3. 将下面列表中的所有字符变为小写：(列表生成式)
#     ['Tom','MIKE','VM','Python']
#     'Tom'.lower()
l = ['Tom','MIKE','VM','Python']
p = [x.lower() for x in l]
print(p)


# 4. 使用迭代查找一个列表中的最大值和最小值，返回一个tuple
def dx(l3):
    (min,max) =(l3[0],l3[0])
    for i in l3:
        if max<i:
           max = i
        if min>i:
           min = i
    return(min,max)
l2 = [6,3,4,5]
print(dx(l2))
# '''     选做题    '''
# 5. 使用生成器构造一个自然数序列
def zran():
    a = 0
    while a<10:
        yield a  
        a += 1

p = zran()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
# print(next(p))  StopIteration
# 6. 使用闭包实现归计数器函数
# def jishu():
#     def m():
#         a = 1
#         while True:
#             yield a
#             a +=1
#     return m
# print(jishu)

# def zj():
#     f = 0
#     def add_one():
#         f = f + 1
#         return f
#     return add_one

# counter = zj()
# print(counter)  
