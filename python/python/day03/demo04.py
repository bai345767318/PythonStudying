'''
生成器 generator
'''

# l = list(range(10))
# l = list(range(100))
# print(l)

m = [x*x for x in range(10)]
print(m)
print(tuple(m))

# 生成器
# 生成器中保存的是算法
g = (x*x for x in range(10))
print(g)

from collections.abc import Iterable
print(isinstance(g,Iterable))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration

# for i in m:
#     print(i)

for i in g:
    print(i)

# 1 2 3 4 5 6 7
# 1 1 2 3 5 8 13...
# def fib(n):
#     m,a,b = 0,0,1
#     while m<n:
#         print(b)
#         a, b = b, a+b
#         # t = (b,a+b)
#         # a = t[0]
#         # b = t[1]
#         m = m+1

# fib(7)
# 生成器
def fib(n):
    m,a,b = 0,0,1
    while m<n:
        yield b  # return b
        a, b = b, a+b
        m = m+1

p = fib(7)
print(p)

print('------------')
for i in p:
    print(i)

# 构造一个完整的fibonacci数列
def fib2():
    a,b = 0,1
    while True:
        yield b  # return b
        a, b = b, a+b

print('************************')
q = fib2()
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
