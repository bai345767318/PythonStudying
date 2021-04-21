'''
输入和输出
'''

# 输出到控制台(console,terminal)
# pyton 中单引号和双引号是等价的
print('welcome to python')
print("Today is rainning")

a = 10
print(a)
print('a=',a)

print(3+2)

# 输入
name = input('请输入您的姓名：')
print(name)
# input()函数的返回值是str类型，如果需要数字，应当进行强制转换--> int()
b = int(input("请输入第一个数字："))
c = int(input("请输入第二个数字："))
print("b+c =",b+c)


