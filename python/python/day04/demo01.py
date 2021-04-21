'''
面向对象编程 Object Oriented Programming - OOP
对象： 万事万物皆对象
类：某一类具有相同属性的对象的抽象
面向对象三大特性：封装，继承，多态
'''

class Student: # 类名首字母大写

    # 方法：写在类里面的函数(function)，称为方法method
    # 构造方法 constructor
    def __init__(self,name,score,gender,height=175): # 方法的第一个参数必须是self
        # self.xxx 就是属性，也是成员变量
        # name 局部变量
        # __xxx 变量前面加__,就变成了私有变量 private,只能在类的内部访问，外部无法访问
        self.__name = name
        self.__score = score
        self.__gender = gender
        self.height = height

    # 方法
    def study(self):
        print('%s正在学习...'%self.__name)

    def show(self):
        print('%s的考试成绩是：%d'%(self.__name,self.__score))

    '''
        封装
        首先将成员变量私有化(self.__xxx)
        然后通过添加get/set方法来访问私有变量
    '''
    # 获取self.__name属性的值
    def get_name(self):
        return self.__name

    # 修改self.__name属性的值
    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if score>=0 and score<=100:
            self.__score = score
        else:
            # 抛出一个异常
            raise ValueError('非法的成绩！')

    # 性别对应的get/set 方法
    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        # if gender=='M' or gender=='F':
        if gender in ['M','F']:
            self.__gender = gender
        else:
            raise ValueError('性别输入错误')

# 调用构造方法创建对象
tom = Student('Tom',90,'M') # 实际调用的就是该类的__init__()方法
julia = Student('Julia',88,'F')

tom.study()
julia.study()

print(tom)
print(julia)
print(Student)

# tom.__name = 'Tommy'
tom.set_name('Tommy')
tom.study()

tom.show()
# tom.__score = 95
tom.show()

julia.show()

# tom.__score = -5
# tom.set_score(500)
tom._Student__score = -100
tom.show()
