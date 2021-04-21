'''异常处理机制'''
'''
异常栈信息
Traceback (most recent call last):
File "d:/workspace/python/day05/demo01.py", line 4, in <module>
    b = 10/a

异常信息
ZeroDivisionError: division by zero
'''

try:
    # 把有可能发生异常的代码放在try代码块中
    a = int(input('请输入一个数字：'))
    b = 10/a
    print('b=%d'%b)
# 捕捉异常时，要注意except从句的顺序，小类型在前，大类型在后
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except Exception as e: 
    # 如果发生了异常，则执行except代码块
    print('Except:',e)
finally:
    # 不管是否发生异常，finally代码块中的代码一定会执行
    print('计算结束！')