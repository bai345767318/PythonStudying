# # 计算BMI指数
w = float(input('请输入你的体重：'))
h = float(input('请输入你的身高：'))
bmi = float(w/h/h)
if bmi<18.5:
    print('太瘦')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('微胖')
elif bmi<32:
    print('肥胖')
else:
    print('死肥宅')

# # # 输出两个int数中最大
a = int(input('整数a：'))
b = int(input('整数b：'))
if a>b:
    print(a)
else:
    print(b)

# # 判断是不是闰年
year = int(input('输入年份:'))
if year % 100 == 0:
    if year % 400 == 0:
        print('是闰年')
    else:
        print('不是闰年')
else:
    if year % 4 == 0:
        print('是闰年')
    else:
        print('不是闰年')


# #3个数中的最大值
a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)


year = int(input('输入年份:'))
if type(year/100) == type(1):
    if type(year/400) == type(1):
        print('是闰年')
    else:
        print('不是闰年')
else:
    if type(year/4) == type(1):
        print('是闰年')
    else:
        print('不是闰年')

print(type(1))
print(type(2020/4),2020/4)
print(type(2000/4),2000/4)
print(type(20/4),20/4)








 