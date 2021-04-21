package day01;

import javax.swing.*;
import java.util.Arrays;

/*
运算符:
python：
    运算符：+ - * /  %
    逻辑运算符：与 或 非 and or not
    关系运算符/比较运算符：== >  <  >=  <=  !=
    赋值运算符：=  += *= /=
    位运算：>>>   <<  >>
java:
    算术运算符：++（自加）  --(自减)
    逻辑运算符：逻辑与：& 、&& 逻辑或：|、|| 非：！
    三元运算符:（表达式）？表达式1：表达式2
 */
public class Demo04 {
    public static void main(String[] args) {
        int i = 10;
        System.out.println(i++);//先使用再自增  10
        //i++等价于i=i+1
        System.out.println(i);//11

        i = 10;
        System.out.println(++i);//先自增再打印

        /*
        逻辑与：&  && 运算结果一样-- 两个效率高
        &&（短路与）：左边是true，会计算右边的表达式；如果左边是false，右边的表达式不计算。
        &：不论左边true/false，右边的表达式都会计算。
         */
        boolean b1 = true;
        int num = 10;
        //左边是true，&/&&右边的表达式都会计算
        if (b1 && num++ <10){
            System.out.println("分支1");
        }
        else {
            System.out.println("分支2");
        }
        System.out.println(num);//11


         b1 = false;
         num = 10;
        //左边是false，&右边的表达式会计算；&&时，右边的表达式不会计算
        if (b1 && num++ <10){
            System.out.println("分支1");
        }
        else {
            System.out.println("分支2");
        }
        System.out.println(num);//10

        /*
        |  ：不管怎样，右边都参与运算
        || 短路或：如果左边为true，右边不参与运算；如果左边为false，右边参与运算。
         */

        /*
        对age >=18的结果取反
        age >=18 :结果为true，取反的话为false。
         */
        int age = 16;
        if (!(age >=18)){//age<18
            System.out.println("age<18");
        }
        else {
            System.out.println("age>=18");
        }
        /*
        三元运算符：（条件表达式）？表达式1：表达式2
        如果条件表达式的结果为true，则返回表达式1，否则返回表达式2
         */
       String s=(age >18)? "大于18":"小于18";
       System.out.println(s);

       int a =10;
       int b = 5;
       int max =(a>b)?a:b;
       System.out.println(max);


    }
}
