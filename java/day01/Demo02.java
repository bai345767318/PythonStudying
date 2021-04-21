package day01;

import java.util.Scanner;

/*
* 输入和输出
*/
public class Demo02 {
    /*main 回车*/
    public static void main(String[] args) {
        /*sout 回车*/
        System.out.println("输出");

        //实例化一个Scanner的对象
        //类似于int a = new Scanner(System.in);
        Scanner scanner = new Scanner(System.in);//表示键盘输入
        //Scanner java.util包里面的一个类
        //new 创建一个实例。
        String name = scanner.next();//读取一个字符串
        System.out.print(name);

        int age = scanner.nextInt();//整数
        System.out.println(age);

        float weight = scanner.nextFloat();//浮点数
        System.out.println(weight);

        /*
        * 练习：键盘输入两个名字，分别存到变量name1、name2中，打印：Hello，name1、name2!*/
        String name1 = scanner.next();
        String name2 =scanner.next();
        System.out.println("Hello,"+name1+","+name2+"!"+10);
        System.out.println("这是一个整数："+100);//支持字符串与其他类型做加法，加号表示拼接
        System.out.println(100+200.1);//300.1
        System.out.println("这是一个整数："+100+300+400);//这是一个整数：100300400
        System.out.println("这是一个整数："+(100+300+400));//这是一个整数：800
        System.out.println(+100+300+400+"这是一个整数");//800这是一个整数


    }
}
