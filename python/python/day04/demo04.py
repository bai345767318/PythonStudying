'''
如何获取对象的信息
'''

# type() 获取对象的类型
print(type(123))
print(type('abc'))
print(type(abs))


# import demo03
# a = demo03.Animal()

from demo03 import Animal

a = Animal()
print(type(a))

print(type(123)==type(456))

print(type(123)==int)

print(type('abc')==str)

def f():
    pass

import types

print(type(f)==types.FunctionType)

# isinstace() 判断某个对象是否是某种类型
print(isinstance('abc',str))


# dir() 获取对象的所有属性和方法
print(dir(a))

print(len(a))# 100

# getattr()/setattr()/hasattr()

from demo01 import Student

s = Student('Tom',90,'M')

# hasattr() 判断对象是否有某个属性
print(hasattr(s,'height'))
# print(hasattr(s,'__name'))
print(hasattr(s,'_Student__name'))

print(dir(s))

# setattr()给属性赋值
setattr(s,'_Student__gender','F')
# getattr()获取属性的值
# print(s.get_gender())
print(getattr(s,'_Student__gender'))