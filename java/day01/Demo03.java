package day01;
/*
变量和数据类型
python：整型、浮点、字符串、布尔、空、列表、元组、字典、集合
java:
    基本的数据类型：8种
        整型：byte、short、int、long
        浮点型：float、double
        字符：char
        布尔：boolean
    引用类型/数组：String、List、Map
*/
public class Demo03 {
    public static void main(String[] args) {
       // python 弱类型的语言，一个变量可以赋值任意类型的值 a = 1 a ="dadsad"
        //java 强类型的语言，定义一个int类型的变量，只能存放int类型的值。
        int a = 10;//定义变量的时候，声明变量的类型
        /*
        整型：byte(占1个字节)、short(占2个字节)、int(占4个字节)、long(占8个字节)
        */
        byte b1 = -128;
        byte b2 = 127;
        //byte b3 = 128；//超过byte取值范围，赋值报错。
        short s1 = -32768;
        short s2 = 32767;
        System.out.println(s1);
        System.out.println(s2);

        //-2的31次方，2的31次方-1
        int i1 = -2147483648;
        int i2 = 2147483647;
        //int i3 = 2147483648;//超出int取值范围

        long long1 = 2147483648L;//赋值时后面加L,表示long类型的数字，L可以大写可以小写，最好用大写
        /*
        浮点类型：float(4字节)、double(8字节)
        */
        float f1 = 3.123F;//给float类型赋值，后面加F/f；
        double d1 = 234.123123;

        /*
        字符：char,单引号，双引号表示字符串
         */
        char c1 = 'a';//字符a
        char c2 ='\n';//换行符
        //"a" 'a' :前面时字符串，后面是字符
        System.out.println(c1);
        char c3 = '\u0061';//unicode,两个字节表示一个字符，表示unicode
        System.out.println(c3);

//        char c4 = 'ab';//非法
//        char c5 = "a";//非法

        /*
        boolean
        */
        boolean bool1 = true;
        boolean bool2 = false;
        if (bool1){
            System.out.println("true");
        }
        else {
            System.out.println("false");
        }
        /*
        类型转化
        自动转换：容量小的类型向容量大的类型转换(小瓶子里的水倒入到大瓶子里)
                byte、char、short -->int-->long-->float-->double
                  1     2     2       4     8       4       8
                  Boolean 不能与其他类型转换
        强制转化：容量大的向容量小的类型转化(大瓶子里的水倒入到小瓶子里，可能存在溢出、数据错误、精度丢失等问题)
         */
        byte bb =2;
        char cc = 'a';//十进制的97
        int dd = bb + cc;//bb cc 自动转换为int后，再计算
        System.out.println(dd);

        //强制转化：(强转的类型)
        long ee = 12345;
        int ff = (int)ee;
        System.out.println(ff);

        ee = 1234567891234L;//超过int的表示范围，导致溢出
        ff =(int)ee;//强转为int
        System.out.println(ff);//1912277282
        //long 64 int 32 只取前面32位
        ff = (byte)ee;
        System.out.println(ff);//34



    }
}
