package day03;

import java.util.Scanner;

/*
练习：
定义一个三角形的类
类名：Triangle
属性：a、b、c三个边长
方法：
    构造方法()
    String triangleType() 返回三角形的类型：一般三角形、等边三角形、等腰三角形、不是三角形

测试类 TestTriangle:
    main方法，设计测试用例测试triangleType方法(边界值、等价类)
 */
public class Demo05 {
}

class Triangle {
    double a;
    double b;
    double c;
    //构造方法
    public Triangle(double a,double b,double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    //返回三角形类型
    public String triangleType() {
        if (a<0 | b<0 |c<0){
            return "输入错误";
        }
            if (a + b > c && a - b < c && b + c > a) {
    //                System.out.println("是三角形");
                if (a == b | b == c | a == c) {
                    if (a == b && b == c) {
                        return "是等边三角形";
                    } else {
                        return "是等腰三角形";
                    }
                } else {
                    return "是普通三角形";
                }
            }else{
                    return "不是三角形";
                }
    }

    }

class TestTriangle{
    public static void main(String[] args) {
        Triangle sanjiao1 = new Triangle(4, 5, 5);
        System.out.println(sanjiao1.triangleType());
        Triangle sanjiao2 = new Triangle(3, 3, 5);
        System.out.println(sanjiao2.triangleType());
        Triangle sanjiao3 = new Triangle(-4, 4, 4);
        System.out.println(sanjiao3.triangleType());
    }
}



