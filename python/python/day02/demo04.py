'''
函数 function
'''

# 计算圆面积
# 定义函数
# f(x) = ax + b
def f(r): # 函数可以定义参数
    PI = 3.1415926
    area = PI*r*r
    print(area)

# 调用函数
f(10)
f(20)

# 内置函数
print(abs(-5))
print(max(1,7))
print(max(1,7,9,33,35,6))
print(int('123'))
print(str(123))
print(bool(1))


'''自定义函数'''
# def 函数名(参数):
#     函数体
#     return


# 自定义绝对值函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-5))
print(my_abs(5))


# 空函数
def g():
    pass

print(g())

import math

# 如果return语句返回多个值，则自动封装为一个元组
def move(x,y,length,angle):
    x1 = x + length*math.cos(angle)
    y1 = y + length*math.sin(angle)
    return x1,y1 # 自动装箱

print(move(10,10,5,math.pi/6))

# 自动拆箱
x,y = move(10,10,5,math.pi/6)
print(x)
print(y)


# 求解一元二次方程
def slove(a,b,c):
    # 求delta
    delta = b**2-4*a*c

    if delta >=0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1,x2
    else:
        print('此方程无解！')

print(slove(1,-7,-18))