package day01;

import java.util.Scanner;

/*
程序的三种控制结构：
循环：for、while、do-while
分支：if-else、switch-case
顺序:
 */
public class Demo05 {
    public static void main(String[] args) {
        int age = 10;
        if(age<0){
            System.out.println("输入的年龄非法");
        }else if (age<18){
            System.out.println("青少年");
        }else if (age<35){
            System.out.println("青年");
        }else if (age<60){
            System.out.println("中年");
        }else {
            System.out.println("老年");
        }




    }
}
/*
一个文件可以有多个类，但只能有一个public类
 */
class Test{
    public static void main(String[] args) {
        /*
        练习：计算狗的年龄。小花家一只狗5岁，计算它相当于人类的多少岁。
        算法：狗的前两年每一年相当于人类的10.5岁，之后每增加一年就增加4岁
        狗的年龄可以键盘输入
         */
        //类似于int a = new Scanner(System.in);
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入狗的年龄：");
        int age1 = scanner.nextInt();
        if (age1<=0){
            System.out.println("输入年龄错误");
        } else if (age1 <=2){
            System.out.println("相当与人的"+(age1*10.5)+"岁");
        }else if (age1>2){
            System.out.println("相当与人的"+((2*10.5)+4*(age1-2))+"岁");
        }

        /*
        switch-case:多分支的语句，判断一个变量是否跟一系列值相等
         */
        Scanner s = new Scanner(System.in);
        System.out.println("请输入季节");
        String season = s.next();
        /*
        season与case的几个分支去匹配，匹配上之后，执行对应的分支。
        break是可选的，把break注释后试试。省略后直到遇到第一个break后退出
         */
        switch (season){
            case "春":
                System.out.println("春暖花开");
//                break;
            case "夏":
                System.out.println("烈日炎炎");
//                break;
            case "秋":
                System.out.println("秋高气爽");
                break;
            case "冬":
                System.out.println("冬雪皑皑");
//                break;
            default:
                System.out.println("季节有误");
                break;
            }
            /*
            练习：输入12个月份，
            如果是11，12，1返回冬季；
            如果是2，3，4返回春季；
            如果是5，6，7返回夏季；
            如果是8，9，10返回秋季；
             */
            Scanner scanner2 = new Scanner(System.in);
            System.out.println("请输入月份");
            int month = scanner2.nextInt();
            switch (month){
                case 11:
                case 12:
                case 1:
                    System.out.println("冬天");
                    break;
                case 2:
                case 3:
                case 4:
                    System.out.println("春天");
                    break;
                case 5:
                case 6:
                case 7:
                    System.out.println("夏天");
                    break;
                case 8:
                case 9:
                case 10:
                    System.out.println("秋天");
                    break;
                default:
                    System.out.println("输入月份有误");
                    break;


            }
    }
}