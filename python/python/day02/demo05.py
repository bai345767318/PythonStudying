'''
函数的参数
'''

'''位置参数 positional argument'''
# 位置参数必须传参
# 位置参数按照顺序传参
def power1(x):
    return x*x

# print(power()) #TypeError: power1() missing 1 required positional argument: 'x'

def power2(x,n):
    s = 1
    while n>0:
        s *= x
        n -= 1
    return s

print(power2(2,3))
print(power2(5,2))

'''默认参数'''
# 默认参数可以不赋值，如果不赋值，则使用默认值
# 默认参数必须放在位置参数的后面
def power3(x,n=2):
    s = 1
    while n>0:
        s *= x
        n -= 1
    return s

print(power3(9,3))
print(power3(9))

def enroll(name,age=7,gender='男'):
    print('%s:%s:%s'%(name,age,gender))

enroll('tom',7,'男')
enroll('mike',6)
enroll('marry',7,'女')
enroll('marry',gender='女',age=6)


'''可变参数'''
# 参数的个数是可变的

# 求任意个数之和
# def sum(x):
#     s = 0
#     for i in x:
#         s += i
#     return s

# print(sum([1,2,3,4,5]))

def sum(*x):
    print(x)
    s = 0
    for i in x:
        s += i
    return s

print(sum(1,2,3,4,5))
print(sum(1,2,3))
print(sum())

# print(sum([1,2,3,4,5]))
l = [1,2,3,4,5]
print(sum(l[0],l[1],l[2],l[3],l[4]))
print(sum(*l))


'''关键字参数'''

def person(name,age,**kw):
    print('name:%s, age:%s,其它:%s'%(name,age,kw))

person('tom',22)
person('mike',22,gender='M',hobby='唱歌',weight=70)


'''命名关键字参数'''
# 命名关键字参数，必须传入参数名

def person2(name,age,*,gender,hobby): # 只要gender和hobby
    print('name:%s, age:%s,gender:%s,hobby:%s'%(name,age,gender,hobby))

person2('julia',18,gender='F',hobby='游泳')
# person2('julia',18,gender='F',hobby='游泳',weight=70)
# person2('julia',18)
# person2('julia',18,'F','游泳')
