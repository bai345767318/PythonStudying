package day02;

import java.util.Arrays;
import java.util.Scanner;

/*
二维数组：可以看作一个一维数组，数组中的元素是一维数组
 */
public class Demo03 {
    public static void main(String[] args) {
        //数组中4个元素，每个元素是一个包含3个元素的数组，4*3的数组
        int[][] arr1 = new int[][] {{1,2,3},{4,5,6},{7,8,9},{10,11,12}};
        System.out.println(arr1[3][2]);//12,前面的[]取值0~3，后面的[]取值0~2
        //for
        for (int i=0;i<arr1.length;i++){
            for (int j=0;j<arr1[i].length;j++){
                System.out.print(arr1[i][j]);
            }
            System.out.println();
        }
        System.out.println("===========分割线=============");
        //foreach
        for (int[] ints : arr1) {//遍历arr1,每个元素是一个一维数组
            for (int anInt : ints) {//遍历一维数组，里面是int类型的值
                System.out.print(anInt);
            }
        System.out.println();
        }
        //练习：定义一个二维数组存放3个人的信息，每个人信息包括：姓名、年龄、身高、体重
        //遍历数组，将每个人的信息打印一行
        //3*4
        String [][] info = new  String[][] {{"张三","18岁","1.80m","75kg"},
                                            {"李四","20岁","1.70m","70kg"},
                                            {"王五","16岁","1.75m","65kg"}};
        //for
        for (int i=0;i<info.length;i++){
            for (int j=0;j<info[i].length;j++){
                System.out.print(info[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("********分隔线********");
        //foreach
        for (String[] strings : info) {
            for (String string : strings) {
                System.out.print(string+" ");
            }
            System.out.println();
        }
        //练习：3个班级，每个班级5个人，键盘录入每个人的成绩，计算每个班级成绩总和。
        Scanner s = new Scanner(System.in);
//        int classes =s.nextInt();
//        float scores = s.nextFloat()；
        float info1[][] = new float[3][5];
        for (int i=0;i<3;i++){
            float sum =0;//
            for (int j=0;j<5;j++){
                System.out.println("请输入"+(i+1)+"班第"+(j+1)+"学生成绩：");
                float scores = s.nextFloat();
                info1[i][j]=scores;
                sum=sum+scores;
//                System.out.println(i+"班成绩"+Arrays.toString(info1[0]));
            }
            System.out.println((i+1)+"班"+"总成绩为："+ sum);
        }
        System.out.println("1班成绩"+Arrays.toString(info1[0]));
        System.out.println("2班成绩"+Arrays.toString(info1[0]));
        System.out.println("3班成绩"+Arrays.toString(info1[0]));







    }
}
