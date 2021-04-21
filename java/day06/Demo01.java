package day06;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

/*
常用类
Math：数学运算方法
Random:生成随机数
Date：日期
 */
public class Demo01 {
    public static void main(String[] args) throws InterruptedException {
        System.out.println(Math.max(1,2));//最大值
        System.out.println(Math.min(1,2));//最小值
        System.out.println(Math.abs(-10));//绝对值
        System.out.println(Math.pow(2,10));//幂运算

        Random random = new Random();
        for (int i=0;i<10;i++){
            int x = random.nextInt();//生成一个随机的整数，为int的取值范围
            System.out.println(x+" ");
        }
        for (int i=0;i<10;i++){
            int x = random.nextInt(10);//生成一个随机的整数，为0~10的取值范围
            System.out.print(x+" ");
        }
        System.out.println();

        //当前时间
        Date date = new Date();
        System.out.println(date);
        /*
        格式化时间：
        y:表示年，yyyy表示用4位表示年
        M：表示月，MM表示用两位数表示月
         */
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日 HH时mm分ss秒");
        System.out.println(sdf.format(date));

        sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        System.out.println(sdf.format(date));
        //自动化时如果设置定时任务的启动时间，获取当前时间后，加一个小的延时，将定时任务设置为这个时间
        //写日志、文件，获取时间作为文件名，或者日志打印时间

        System.out.println(date.getTime());
        //把时间转化成时间戳。1970年1月1日，08：00：00 作为0时，相对这个时间的秒数。

        long begin = (new Date()).getTime();
        func1();
        long end = (new Date()).getTime();
        System.out.println("执行func1耗时："+(end-begin));
    }
    //模拟一个功能函数，看调用该函数耗时多久
    public static void func1() throws InterruptedException{
        System.out.println("in func1");
        Thread.sleep(1000);//等待1秒
        System.out.println("out func1");
    }
}
