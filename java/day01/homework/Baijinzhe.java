package day01.homework;

import java.util.Scanner;

public class Baijinzhe {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

//第一题：
//        System.out.println("请输入年份:");
//        int year = s.nextInt();
//        int n = year%12;
//        switch (n){
//            case 1:
//                System.out.println("鸡");
//                break;
//            case 2:
//                System.out.println("狗");
//                break;
//            case 3:
//                System.out.println("猪");
//                break;
//            case 4:
//                System.out.println("鼠");
//                break;
//            case 5:
//                System.out.println("牛");
//                break;
//            case 6:
//                System.out.println("虎");
//                break;
//            case 7:
//                System.out.println("兔");
//                break;
//            case 8:
//                System.out.println("龙");
//                break;
//            case 9:
//                System.out.println("蛇");
//                break;
//            case 10:
//                System.out.println("马");
//                break;
//            case 11:
//                System.out.println("羊");
//                break;
//            case 12:
//                System.out.println("猴");
//                break;
//            default:
//                System.out.println("输入错误!");
//            }

//第二题：
//        System.out.println("请输入学生成绩");
//        int fs = s.nextInt();
//        if (fs >= 90 && fs <=100){
//            System.out.println("A");
//        }else if (fs >=70 && fs <90){
//            System.out.println("B");
//        }else if (fs >=50 && fs <70){
//            System.out.println("C");
//        }else if (fs >=0 && fs <50) {
//            System.out.println("D");
//        }else {
//            System.out.println("成绩输入的有毛病,老铁！");
//        }

//第三题：
//        System.out.println("请输入您的会员卡号第一位：");
//        int num1 = s.nextInt();
//        System.out.println("请输入您的会员卡号第二位：");
//        int num2 = s.nextInt();
//        System.out.println("请输入您的会员卡号第三位：");
//        int num3 = s.nextInt();
//        System.out.println("请输入您的会员卡号第四位：");
//        int num4 = s.nextInt();
//        if ((num1+num2+num3+num4)==25){
//            System.out.println("恭喜您中奖了");
//        }else {
//            System.out.println("很遗憾您没中奖！");
//        }

//第三题：
        System.out.println("请输入4位数会员卡号：");
        int id = s.nextInt();
        if (1000<=id && id<=9999){
//            System.out.println("输入合法");
            int a = id/1000;
//            System.out.println(a);
            int b = (id/100)%10;
//            System.out.println(b);
            int c = (id/10)%10;
//            System.out.println(c);
            int d = id%10;
//            System.out.println(d);
            int sum = a+b+c+d;
            if (sum==25){
                System.out.println("恭喜中奖");
            }else  {
                System.out.println("很遗憾没中奖");
            }
        }else {
            System.out.println("输入不合法");
        }



    }
}


