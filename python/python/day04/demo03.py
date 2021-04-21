'''
多态
'''

class Animal(object): # 默认继承object类

    def __len__(self):
        return 100

    def run(self):
        print('Animal is running...')

class Dog(Animal):
    
    def eat(self):
        print('Dog is eatting bone...')

    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

a = Animal()
dog = Dog()
cat = Cat()

print(isinstance(1,int))
print(isinstance(1,str))

print(isinstance(a,Animal))
print(isinstance(dog,Dog))
print(isinstance(cat,Cat))

print(isinstance(dog,Animal))  # True
print(isinstance(a,Dog)) # False


def run_twice(animal:Animal):
    animal.run() # 表面上调用的是父类的run()方法，实际执行的是子类的run()方法
    animal.run()

run_twice(a)
run_twice(dog)
run_twice(cat)

class Turtle(Animal):

    def run(self):
        print('Turtle is crawling...')

run_twice(Turtle())