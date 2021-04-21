package day04;
/*
抽象类：
    抽象方法：是只有声明，没有实现。含有抽象方法的类是抽象类。使用abstract-摘要关键字修饰。
    抽象类不能实例化。抽象类存在的目的主要是为了继承。
    抽象方法相当于定义了一种规范，从抽象类(Animal)继承的子类(Fish)，必须实现抽象方法(eat)。

 */
public class Demo04 {
    public static void main(String[] args) {
//        Animal a = new Animal();//抽象类不能实例化。
        Animal a = new Fish();//继承关系后的实例化--父类不能实例化，所以用子类实例化
        a.eat();
        a.run();
        Fish b =new Fish();
        b.eat();
        b.run();

    }
}
//抽象类
abstract class Animal{
    //非抽象的方法,声明+实现，{}内的内容为方法的实现。
    public void run(){
        System.out.println("跑......");
    }
    //抽象的方法，只有声明，没有实现.
    public abstract void eat();
}
class Fish extends Animal{
    //子类要实现父类定义的抽象方法，否则子类也必须定义为抽象类。--看提示
    // 要么把要继承的类改写为抽象类，要么把方法重写并实现
    //重写
    @Override
    public void eat() {
        System.out.println("fish eat......");
    }
}
