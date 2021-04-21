package day04;
/*
常用关键字
this:实例,this.属性;this.方法
super:父类,super.方法() 构造方法-->demo02
static:修饰方法,静态方法,类名.方法;修饰成员变量,静态的变量,类名.变量。
final:修饰类时不能被继承;修饰方法时，方法不能被子类重写;修饰变量时，变量只能被赋值一次。
 */
public class Demo07 {
    public static void main(String[] args) {
        Voter zhang = new Voter("张明");
        zhang.vote();
        System.out.println("当前投票数量"+Voter.count);//静态变量的使用 类名.变量名 访问。

        for (int i=0;i<25;i++){
            Voter v = new Voter("选民"+i);
            v.vote();
            System.out.println("当前投票数量："+Voter.count);
        }
    }
}

class Voter{
    static int count;//投票的数量，所有选民共享这一数据。
    String name;//选举人的名字，每个选民每人有一个名字。
    //构造方法
    public Voter(String name){
        this.name = name;
    }
    //计票的方法，投票数量达到20票，则停止投票
    public void vote(){
        if (count==20){
            System.out.println("投票结束");
        }else {
            count++;
            System.out.println(this.name+",感谢投票");
        }
    }
}
final class A{}
//class B extends A{} //报错 final:修饰类时不能被继承
class B {
    public static final float PI=3.14f;//常量的定义 Math.PI
    public final void func(){
        final String name;
        name = "A";

//        name = "B";//报错 修饰变量时，变量只能被赋值一次。
    }
}
class C extends B{

//    public void func(){} //报错 final修饰方法时，方法不能被子类重写
}