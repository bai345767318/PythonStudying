'''
继承
1. 子类继承父类的方法
2. 子类还可以有自己独有的方法
3. 子类的方法可以覆盖父类的同名方法
'''

class Animal(object): # 默认继承object类

    def run(self):
        print('Animal is running...')

# Dog类(子类)继承了Animal类(父类)
class Dog(Animal):
    
    def eat(self):
        print('Dog is eatting bone...')

    # 子类的同名方法会覆盖父类的同名方法
    def run(self):
        print('Dog is running...')

dog = Dog()
dog.run()
dog.eat()

class Cat(Animal):
    pass

cat = Cat()
cat.run()