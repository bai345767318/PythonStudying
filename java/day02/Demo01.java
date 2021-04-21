package day02;

import java.util.Scanner;

/*
循环：for、while、do-while
 */
public class Demo01 {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hello World");
        }
        //for(a初始化条件;b循环条件;c迭代条件)
        //d循环体
        //a->b->d->c->b->d->c->b->d->c
        //i是局部变量，作用域是在for循环内部，出了作用域不生效。
        //System.out.println(i);

        //ctrl+alt+L:格式化代码

        //练习：遍历100以内的偶数，计算偶数的个数和和。
        int num = 0;
        int sum = 0;
        for (int i = 0; i <= 100; i += 2) {
            num++;
            sum += i;
        }
        System.out.println("和:" + sum);
        System.out.println("个数:" + num);

        //100-0倒着遍历
        for (int i = 100; i >= 0; i--) {
            System.out.println(i);
        }

        //打印5个星，每次打印一个打印6行
        for (int i = 0; i < 6; i++) {//这层循环控制行，共6行
            for (int j = 0; j < 5; j++) {//这层循环控制列，每行5列
                System.out.print("*");
            }
            System.out.println();//每行末的换行符
        }
        //*
        //**
        //***
        //****
        //*****
        for (int i = 0; i <= 5; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        //*****
        //****
        //***
        //**
        //*
        for (int i = 0; i < 6; i++) {//行
            for (int j = 5; j > i; j--) {//列
                System.out.print("*");
            }
            System.out.println();
        }

        //100以内偶数的个数及所有偶数的和
        int i = 0;//初始化条件
        int c = 0;//计算个数
        int s = 0;//计算和
        while (i <= 100) {//循环条件,满足条件,执行循环体;不满足,跳出循环.
            c++;//循环体
            s = s + i;
            i = i + 2;//迭代条件,迭代条件如果忘记写，就会导致死循环。
        }
        System.out.println("偶数的个数为：" + c + "所有偶数的和为：" + s);

        //
        i = 0;//初始化条件
        c = 0;
        s = 0;
        do {
            c++;//循环体
            s = s + i;
            i = i + 2;//迭代条件
        }while (i<=100);//循环条件
        System.out.println("偶数的个数为：" + c + "所有偶数的和为：" + s);
        //while:先判断是否满足循环条件，再去执行循环体
        //do-while:先执行循环体，再判断条件是否满足，循环体至少被执行一次
        i = 0;
        while (i>10){
            System.out.println("while循环体，此句执行不到");

        }
        do {
            System.out.println("do-while循环体，执行一次");
        }while (i>10);

        /*
        break:结束整个循环
        continue:结束本次循环
         */
        for (i = 1;i<=10;i++){
            if (i%4==0){//i%4==0,即4的倍数
//                break;//123
                continue;//123567910
            }
            System.out.print(i);
        }

        System.out.println();
        aaa:
        for (int j=0;j<4;j++) {
            for (i = 1; i <= 10; i++) {
                if (i % 4 == 0) {//i%4==0,即4的倍数
//                    break;//123 123 123 123 跳出包含这个关键字的最近一层循环
//                    continue;//123567910 123567910 123567910 123567910
//                    break aaa;//123 结束指定标识的一层的循环--外
                    continue aaa;//123 123 123 123 结束指定标识的一层当次的循环-内
                }
                System.out.print(i);
            }
        }
        //练习：循环从键盘输入某个学生5门课的成绩，计算总分，如果输入的成绩为负数，结束循环。
        Scanner scanner= new Scanner(System.in);
        sum = 0;
        for (i=1;i<=5;i++){
            System.out.println("请输入第"+i+"科成绩:");
            int grade = scanner.nextInt();
            if (grade<0){
                System.out.println("您的成绩输入有误");
                break;
            }
            sum = sum +grade;
            if (i==5){
                System.out.println("总分:"+sum);
            }
        }
//        System.out.println("总分:"+sum);



    }
}
