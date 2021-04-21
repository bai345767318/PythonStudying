'''
实例属性和类属性
实例：instance
'''

class Person:

    # 类属性
    name = '人类'
    count = 0

    def __init__(self,name,age):
        # 实例属性
        self.name = name
        self.age = age

# 创建Person类的一个实例p
p1 = Person('张三',22)
Person.count += 1
print(p1.name,p1.age)
p2 = Person('李四',23)
Person.count +=1

print(p2.name,p2.age)

# 类属性可以通过类名直接访问
print(Person.name)
# 类属性也可以通过该类的实例对象来访问
print(p1.count)
print('*****************')
# 如果类属性的名字和实例属性的名字重名，则实例对象只能实例属性，访问类属性只能通过类名
print(p1.name)
print(Person.name)

print(Person.count)

p1.gender = 'Male'
print(p1.gender)

