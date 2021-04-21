# 定义一个函数，计算任意个数字的乘积

# def chengji(*n):
#     s = 1
#     for i in n:
#         s *= i
#     return s
# print(chengji(1,2,3,4,5))

# 数列求和,有数列为：9，99，999，...，9999999999。要求使用程序计算此数列的和，并在控制台输出结果。
# def sum2(m):
#     s = 0
#     n = 1
#     while n<=m:
#         i = (10**n)-1
#         s =s+i
#         n =n+1
#     return s
# print(sum2(1))
# print(sum2(2))

# 有数列：1+1/2+1/3…+1/n（n>=2）。要求使用交互的方式计算此数列的和：用户在控制台录入需要计算的整数 n 的值，程序计算此数列的和，并在控制台输出结果。
# n = int(input('输入数字：'))
# def f(n):
#     if n==2:
#         return 3/2
#     return f(n-1)+1/n
# print(f(n))

# 打印九九乘法表
# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%s*%s=%s" %(y,x,x*y),end=" ")
#     print("")

# 使用冒泡排序法对下面的列表进行升序排序:
a = [23,8,33,4,88]
def sort(x):
    changdu = len(a)
    for i in range(changdu-1):# 外循环每一次使得有序的数增加一个
        for j in range(changdu-1-i):#内循环每次将无序部分中的最大值放到最上面
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
    return x
print(sort(a))



# 斐波那契数列
# n = int(input('输入数字:'))
# list1 =[]
# def f(n):
#     if n==1 or n==2:   
#         return 1          
#     return f(n-2)+f(n-1)
# list1.append(f(n))
# print(list1)


#  用递归实现汉诺塔游戏
    # 输出结果：
    # A —> B
    # A -> C
    # B -> C
    # move(n,a,b,c)
# def move(n, a, b, c):
#     print('9')
#     if n==1:
#         print(a,'到',c)
#         return
#     else:
#         print('0')
#         move(n-1,a,c,b)  #首先需要把 (N-1) 个圆盘移动到 b,计算机怎么识别出这句话是啥意思的。
#         print('1')
#         move(1,a,b,c)    #将a的最后一个圆盘移动到c
#         print('2')
#         move(n-1,b,a,c)  #再将b的(N-1)个圆盘移动到c
#         print('3')
# move(4, 'A', 'B', 'C')




    
