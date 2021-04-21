package day03;
/*
方法：
1.方法可以带参数，可以不带参数，带参数的可以带任意类型的参数。
2.方法可以有返回值，也可以无返回值，可以返回任意类型的值。
3.方法支持可变参数，参数个数可以是1个，2个，多个。python可变参数：*args
4.同名的方法：Python中，后面写的覆盖前面的，JAVA中支持同名的方法，叫方法的重载。
    重载：一个类中，允许存在多个同名的方法，但是他们的参数个数、参数类型、参数顺序要不同。
    重载的好处：调用起来比较简单。println是重载的方法。
 */
public class Demo02 {
    //加法有可变参数，用...表示
    //如果有多个参数，可变参数放最后一个
    //一个方法中，最多只能有一个可变参数
    public int add(int ... nums){
        int sum = 0;
        for(int i =0;i<nums.length;i++){
            sum=sum+nums[i];
        }
        return sum;
    }
    public  float add(float f1,float f2){
        System.out.println("float add");
        return f1+f2;
    }
    public  double add(double f1,double f2){
        System.out.println("double add");
        return f1+f2;
    }


    public static void main(String[] args) {
        Demo02 d = new Demo02();
        System.out.println(d.add());//0
        System.out.println(d.add(1));//1
        System.out.println(d.add(1,2,3,4,5));//15
        System.out.println(d.add(10,20,30));//60

        System.out.println(d.add(10.1f,10.2f));//20.3
        System.out.println(d.add(10.11111111f,10.2f));//20.311111  6位
        System.out.println(d.add(10.1,10.2));//20.299999999999997  15位
    }
}
/*
练习：定义3个重载的方法，求最大值
两个int值返回最大
三个double值返回最大
两个double值返回最大
 */
class Max{

    public int max(int a,int b){
        if (a>b){
            return a;
        }else
            return b;
    }
    public  double max(double a,double b,double c) {
//        double max = a > b ? a : b;
//        return max > c ? max : c;

//        if (a > b && a > c) {//判断a是不是最大值，如果是，返回a
//            return a;
//        } else {
//                if (b>c){//比较b和c
//                return b;
//            } else {
//                return c;
//            }
//        }

        double max =a;
        if (b>max){
            max =b;
        }if (c>max){
            max=c;
        }
        return max;

    }
    public double max(double a,double b){
        if (a>b){
            return a;
        }else
            return b;
    }

    public static void main(String[] args) {
        Max r = new Max();
        int c =r.max(5,4);
        System.out.println("int:"+c);
        double d =r.max(3.1,6.6);
        System.out.println("double:"+d);

        double e =r.max(3,5,2);
        System.out.println("double3:"+e);
    }
}