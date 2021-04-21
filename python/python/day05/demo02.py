'''
Input/Output 输入输出
'''

'''读取文本文件'''

try:
    # open()打开文件，函数的第一个参数是文件路径，以字符串形式出现
    # open()函数默认使用gbk编码集
    file = open(r'D:\workspace\python\day05\test.txt','r',encoding='utf-8')

    # 读取文件
    content = file.read()
    print(content)

except Exception as e:
    print(e)
finally:
    # 关闭文件
    # 除了False以外,诸如 0,None,'',undefined 都当做False; 
    # 其它的所有值当做True
    if file: 
        file.close()

print('----------------------')
# 简化的读写方式 - 自带try-except
with open(r'D:\workspace\python\day05\test.txt','r',encoding='utf-8') as file:
    # read()方法一次性读取全部内容
    # content = file.read()
    # print(content)

    # read(size)
    # content = file.read(9)
    # print(content)

    # readline()方法每次读取一行
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())

    # readlines()方法一次性按行读取所有内容，封装为一个列表,每一行就是一个列表元素
    content = file.readlines()
    print(content)


'''读取二进制文件'''

# img = open(r'D:\workspace\python\day05\Tulips.jpg','rb')
# content = img.read()
# print(content)


