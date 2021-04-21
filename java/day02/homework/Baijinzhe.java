package day02.homework;

import java.util.Arrays;
import java.util.Scanner;

public class Baijinzhe {
    public static void z01() {
        //第一题(方法1)
//        long sum =0;
//        for (int i=0; i<10; i++){
//            long sumj=0;
//            for (int j=0;j<=i;j++){
//                sumj+=Math.pow(10,j)*8;
//            }sum+=sumj;
////            System.out.println(sumj);
//       }
//        System.out.println(sum);

        //第一题(方法2)
        long f =0;
        long sum =0;
        for(int i=0;i<10;i++){
            f = f*10+8;
//            System.out.println(f);
            sum = sum +f;
        }
        System.out.println(sum);

    }
    public static void z02() {
        //第二题
        Scanner s = new Scanner(System.in);
        System.out.println("请输入：");
        int a = s.nextInt();
        int[] b = new int[3];
        b[0] = a;
        b[1] = a * a;
        b[2] = a * a * a;
        System.out.println(Arrays.toString(b));
    }
    public static void z03(){
        //第三题
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j + "*" + i + "=" + i * j + "\t");
            }
            System.out.println();
        }
    }
    public static void z04(){
        //第四题
        Scanner s = new Scanner(System.in);
        float info1[][] = new float[3][5];
        for (int i = 0; i < 3; i++) {
            float sum1 = 0;//
            for (int j = 0; j < 5; j++) {
                System.out.println("请输入" + (i + 1) + "班第" + (j + 1) + "学生成绩：");
                float scores = s.nextFloat();
                info1[i][j] = scores;
                sum1 = sum1 + scores;
//                System.out.println(i+"班成绩"+Arrays.toString(info1[0]));
            }
            System.out.println((i + 1) + "班" + "总成绩为：" + sum1);
        }
        System.out.println("1班成绩" + Arrays.toString(info1[0]));
        System.out.println("2班成绩" + Arrays.toString(info1[1]));
        System.out.println("3班成绩" + Arrays.toString(info1[2]));

    }

    public static void main(String[] args) {
        z01();
        z02();
        z03();
        z04();
    }

}
