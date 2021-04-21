'''递归函数'''

# n!= 1*2*3*4*5*...*(n-1)*n
# 方案1
def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s

print(fact(3))
print(fact(5))

# 方案2（递归）
# n! = (n-1)!*n
# (n-1)! = (n-2)!*(n-1)
# ...
# 2! = 1!*2
# 1!= 1

def f(n):
    if n==1:    # 2.边界条件
        return 1
    return f(n-1)*n # 1.自己调用自己

print(f(3))
print(f(5))

