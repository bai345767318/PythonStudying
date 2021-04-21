package day03;

import java.util.Arrays;

/*
构造方法：类似python中的__init__方法
如果不写构造方法，类里默认有一个无参的构造方法。
如果有构造方法，默认的无参构造方法就没有了
 */
public class Demo03 {
    public static void main(String[] args) {
        //Animal()调用构造方法，实例化
        Animal a = new Animal("李明",10);
        System.out.println(a.name);
        System.out.println(a.age);
        //构造方法的重载，让对象的创建更加灵活。
        Animal cat = new Animal("加菲猫");
        System.out.println(cat.name);
        System.out.println(cat.age);
    }
}

/*
动物类
 */
class Animal{
    String name;
    int age;
    /*
    1.构造方法与类名相同。
    2.构造方法无返回值，不能使用return语句。
    3.构造方法可以重载
     */
    public Animal(String n,int a){
        name = n;
        age = a;
    }
    public Animal(String n){
        name = n;
    }
}

class Dog{
    String name;//成员变量，属性。
    int age;
    String pinzhong;

    //构造方法的代码可以自动生成
    //右键Genarate
    public Dog(String name, int age, String pinzhong) {
        //String name 局部变量,name作用域只在花括号内部。
        //this.name 表示属性。
        //this.name = name;将局部变量赋值给属性name。
        //this表示实例，用来区分成员变量还是局部变量。
        this.name = name;
        this.age = age;
        this.pinzhong = pinzhong;
    }

    public Dog(String name){
        this.name = name;
    }
    @Override
    //所有类都是从Object继承的，如果不写toString，会调用Object中定义的toString方法。
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", pinzhong='" + pinzhong + '\'' +
                '}';
    }


    public static void main(String[] args) {
        Dog wangcai = new Dog("旺财");
        Dog langgou = new Dog("小黑",2,"狼狗");
        System.out.println(wangcai.toString());
        System.out.println(langgou.toString());

    }
}
/*
练习：
定义一个学生类：
1.属性：姓名、班级、分数
2.有一个构造方法
3.有一个toString方法
 */
class Students{
    String name;
    int classes;
    double score;

    public Students(String name, int classes,double score){
        this.name = name;
        this.classes = classes;
        this.score = score;
    }

    @Override
    public String toString() {
        return "Students{" +
                "name='" + name + '\'' +
                ", classes=" + classes +
                ", score=" + score +
                '}';
    }

    public static void main(String[] args) {
        //实例化3个学生，把学生加入数组中
        Students[] students = new Students[3];
        Students lisi = new Students("李四", 2, 59.5);
        Students zhangsan = new Students("张三", 1, 60);
        Students wangwu = new Students("王五", 4, 75);
        students[0] = lisi;
        students[1] = zhangsan;
        students[2] = wangwu;
        System.out.println(Arrays.toString(students));
//        System.out.println(lisi.score);
//        System.out.println(lisi.toString());

    }
}
