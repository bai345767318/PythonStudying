package day04;
/*
接口：接口是一个纯粹的抽象类，里面的方法全部是抽象方法，接口使用interface关键字修饰。
接口:接口是抽象类，但抽象类不是接口，接口不存在继承关系;区别于接口测试，
 */
public class Demo05 {
}
//接口
interface Fly{
//    interface  中所有的接口默认都是publica abstract修饰的，所以可以不写
//    飞翔的接口
    public abstract void fly();
}
//鸟具有飞翔的功能，实现飞的接口。
//接口的实现类 implements:使xx实现
class Bird implements Fly{

    @Override
    public void fly() {
        System.out.println("鸟儿飞");
    }
}
class Plane implements Fly{

    @Override
    public void fly() {
        System.out.println("飞机飞");
    }
}