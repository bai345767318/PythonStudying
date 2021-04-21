'''
数据类型和变量
'''

'''数据类型'''
# 整数
a = 100
b = -5
c = 0b01010100010101  # 二进制整数
print(c)
d = 0o10 # 八进制
print(d)
e = 0xab12f # 十六进制
print(e)

# 浮点数
f = 123456789.0
g = 1.23456789e8  # 科学计数法
h = 123.45678926 
print(g)

# 字符串
i = 'abc' # 用单引号
j = "xyz" # 用双引号
k = "I'm fine"
print(k)
# \ : 转义字符
l = 'I\'m fine'
print(l)
m = 'I\'m\n fine' # \n 回车键
print(m)
n = 'I\'m\t fine' # \t tab键
print(n)
# 输出 \
print('\\')
# 输出 \\\t\\
print(r'\\\t\\')

# 布尔值
o = True
p = False
print(3>1)

# 逻辑运算
# and or not 
print(True and True)
print(3>5 or 6>4)
print(not True)

# 空值
q = None
print(q)
# r # 未定义
# print(r)

'''变量'''
# 数据有类型，变量没有类型
# python是动态语言
x = 1
y = 'abc'
x = 'tom'

# =是赋值符号
x = 'abc'
y = x
x = 'def'
# y=?
print('y=',y)

'''常量'''
# 常量的全部字母大写
PI = 3.1415926
PI = 5
print(PI)