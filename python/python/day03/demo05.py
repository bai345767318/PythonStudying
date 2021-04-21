'''
函数式编程 Functional Programming
函数式编程就是高度抽象的编程范式
'''

'''高阶函数'''

'''函数作为参数'''

print(abs(-10)) # abs():调用函数abs
print(abs)  # abs:指的是函数abs本身

# 函数本身也可以看做一个特殊的值，这个值用函数名表示
# 函数名就是一个变量，这个变量指向函数本身
a = abs
print(a)
print(a(-5))
# abs = -10
# print(abs)
# print(abs(-10))

# 函数作为参数进行传递 我们把这样的函数称为高阶函数

def add(x,y,f):
    return f(x)+f(y)

print(add(3,4,abs))
print(add(3,-4,abs))

def f(x):
    return x*x

print(add(3,4,f))

# map()
l = list(range(10))
r = map(f,l)
print(l)
print(list(r))
print(list(map(str,range(10))))

# reduce() 对参数序列中元素进行累积
#from functools import reduce
#函数，有两个参数    可迭代对象 可选，初始参数 
# reduce(function, iterable[, initializer])

# filter() 用于过滤序列，第一个为函数，第二个为序列

# sorted()


'''返回函数'''

def s(*args):
    x = 0
    for i in args:
        x += i
    return x

print(s(1,2,3))

''' 闭包 closure
lazy_s(外部函数)函数中定义了函数s(内部函数),内部函数s可以引用外部函数的参数(args)和局部变量
当lazy_s返回s的时候，相关的参数和变量都保存在返回的函数中，这种结构就称为"闭包"  装饰器也是一种闭包函数
'''
def lazy_s(*args):
    def s():
        x = 0
        for i in args:
            x += i
        return x
    return s    # 返回了一个函数作为返回值
print('---------------')
a = lazy_s(1,2,3) #<function lazy_s.<locals>.s at 0x000000000263DF70>
print(a())
a = lazy_s(3,6,9)
print(a())


'''匿名函数'''
print(list(map(f,[1,2,3])))
# lambda表达式 ，其实就是一个函数
# def f(x):
#    return x*x
print(list(map(lambda x:x*x,[1,2,3])))

b = lambda x:x*x
print(b)
print(b(5))
