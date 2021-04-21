package day03;
/*
面向过程：最小单位是函数，是按照操作步骤来实现的。
        1.打开冰箱门 2.把大象放进冰箱 3.关上冰箱门 （每一步封装成函数）
面向对象：把功能封装进对象，以类/对象为最小单位来考虑的。
        有哪些对象，每个对象有什么样的行为
        大象：进入（冰箱）
        冰箱：开门、关门
        人：打开（冰箱）、关闭（冰箱）、操作（大象）
类：抽象的概念，相同属性和方法的一组对象的集合。人是一个类，特朗普是具体的实例。
 */
public class Demo01 {
    public static void main(String[] args) {
        //实例化
        Person hua = new Person();
        hua.name = "AA";
        hua.name = "樱木花道";//调用属性，实例.属性  覆盖改值
        hua.age = 16;
        hua.gao = 1.86;
        hua.zhong =75;
        hua.eat();//调方法，实例.方法()
        hua.sleep();
        hua.read("西游记",80);
        //定义一个变量，接收返回值
        int age1 = hua.getAge();
        System.out.println("age1:"+age1);

        //实例化：流川枫
        Person lcf = new Person();
        lcf.name = "流川枫";

        lcf.gao = 1.8;
        lcf.zhong = 73;
        lcf.eat();
        lcf.sleep();
        lcf.read("红楼梦",10);
        int age2 = lcf.getAge();
        System.out.println("age2:"+age2);//0 因为age没实例属性
    }
}
/*
人类：数据类型
 */
class Person{
    //属性：成员变量，属于每一个实例的。   不同于局部变量
    // 创建对象的时候，创建的成员变量，对象销毁时，成员变量才会释放。
    String name;
    int age;
    double gao;
    double zhong;
    //方法
    //public 修饰符表示公共的，private私有的、protected受保护的。
    //void 返回值的类型
    //eat 方法名（）表示无参数
    public void eat(){
        System.out.println(name+"正在吃饭");
    }
    public void sleep(){
        System.out.println(name+"正在睡觉");
    }
    //String book ：参数，String是参数类型，book是参数名
    //int age：参数，int是参数类型，page是参数名
    //可以带任意类型的参数
    public void read(String book,int page){
        System.out.println(name+"正在看"+book+",看到了"+page+"页");
    }
    //int表示这个方法返回int类型的数据
    //通过return返回
    public int getAge(){
        return age;
    }
}

/*
练习：
定义一个类：圆 circle
属性：半径r
方法：计算面积，计算周长

测试这个类：
实例化两个圆，分别计算面积和周长
常量：Math.PI
 */
//class Circle{
//    public static void main(String[] args) {
//        Circle y1 = new Circle();
//        Circle y2 =new Circle();
//        y1.getZc(10);
//        y1.getMj(10);
//        y2.getZc(2);
//        y2.getMj(2);
//    }
//
//    public void getZc(float r){
//        float zc = (float) (2*Math.PI*r);
//        System.out.println("圆的周长："+zc);
//    }
//    public void getMj(float r){
//        float mj = (float) (Math.PI*(r*r));
//        System.out.println("圆的面积"+mj);
//    }
//}
//定义在类内方法外：成员变量/全局变量
//            方法内：局部变量