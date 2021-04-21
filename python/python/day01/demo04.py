'''字符串和编码'''

# 编码
# ASCII American Standard Code for Information Interchange
a = 'a'

# 中文编码
# GB2312 GBK
# unicode universal code 宇宙码 2byte
# utf-8 1-3个字节

# 查看字符的编码
print(ord('a'))
print(ord('A'))
print(ord('中'))

print(chr(97))
print(chr(28888))

# 进制转换
a = 16
print('a =',a)
print('a =',bin(a)) # binary
print('a =',oct(a))
print('a =',hex(a))
print('a =',int(0xf))

c1 = 'china'.encode('ascii') # b: byte
print(c1)
print(len(c1))
c2 = '中国'
print(len(c2))
print(c2.encode('utf-8'))
print(len(c2.encode('utf-8')))

# 字符串格式化
name = input('请输入你的姓名:')
age = input('请输入你的年龄:')
# 我叫tom，今年22岁
print('我叫',name,'今年',age,'岁')
# %s 代表一个字符串
# %d 代表一个整数
# %f 代表一个浮点数
print('我叫%s，今年%d岁'%(name,int(age)))
print('我叫%s，今年%s岁'%(name,int(age))) # %s永远可以用
print('我叫{0}，今年{1}岁'.format(name,age))