package day03.homework;

import java.util.Arrays;

import java.util.Scanner;

public class Baijinzhe {
}

class Z01{
    public static void main(String[] args) {
        //1.数字1、2、3、4能组成多少个互不相同且无重复数字的三位数字？将结果存到数组。
        int[] list = new int[24];
        int m = 0;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                if (i == j) continue;
                for (int k = 1; k <= 4; k++) {
                    if (k == i || k == j) continue;
                    int num = i * 100 + j * 10 + k;
//                    System.out.println(num);
                    list[m++] = num;
                }
            }
        }
        System.out.println(Arrays.toString(list));
        System.out.println();
    }
}

class Z02{
    public static void main(String[] args) {
        //2.数字转汉字 
        //用户输入一个1~9（包含1和9）之间的任一数字，程序输出对应的汉字。如输入2，程序输出“二”。可重复查询。
        Scanner s = new Scanner(System.in);
        System.out.println("请输入1-9的数字：");
        int num = s.nextInt();
        String[] num1 = new String[]{"一","二","三","四","五","六","七","八","九"};
        String n = num1[num-1];
        System.out.println(n);
    }
}

class Z03{
    public static void main(String[] args) {
        //3.假设10位评委的打分是99,80,86,89,94,92,75,87,86,95，
        //去掉一个最高分，去掉一个最低分，计算平均分，并打印出来。
        //打印格式为：
        //去掉一个最高分：XX分，去掉一个最低分：XX分，最后得分为：XX分
        int[] a = {99,80,86,89,94,92,75,87,86,95};
        Arrays.sort(a);
        System.out.println("去掉一个最高分"+a[9]);//最高分
        System.out.println("去掉一个最低分"+a[0]);//最低分
        int sum =0;
        double p = 0;
        for (int i=1;i<a.length-1;i++){
            System.out.print(a[i]+" ");
            sum = sum +a[i];
            p = sum/(a.length-2);
        }
        System.out.println("最终得分："+p);
    }
}

//4.练习：
//定义一个三角形的类：
//类名：Triangle
//属性：a、b、c三个边长
//方法：
//   构造方法()
//   String triangleType() 返回三角形的类型：一般三角形、等边三角形、等腰三角形、不是三角形
//
//测试类 TestTriangle：
//   main方法，设计测试用例测试triangleType方法（边界值、等价值）
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
        if (a<=0 | b<=0 |c<=0){
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
        Triangle sanjiao1 = new Triangle(0, 5, 5);
        System.out.println(sanjiao1.triangleType());
        Triangle sanjiao2 = new Triangle(3, 3, 5);
        System.out.println(sanjiao2.triangleType());
        Triangle sanjiao3 = new Triangle(-4, 4, 4);
        System.out.println(sanjiao3.triangleType());
    }
}
