package day05;
/*
包装类:
int:4 Integer
char:2 Character
float:4 Float
double:8 Double
boolean:1 Boolean
long:8 Long
short:2 Short
byte:1 Byte
8种基本类型不是面向对象的编程机制。保留这些类型是为了照顾程序员的使用习惯。
为了解决8种基本类型不能当作对象使用的问题，java提供了包装类。
包装类的作用：
    1.提供了一系列使用的方法，字符串转整数 int(python)
    2.集合list、Map、Set，集合不允许放基本类型，比如存放数字时，不能放int类型的，只能放Inteager类型的。
 */
public class Demo02 {
    public static void main(String[] args) {
        Integer num = new Integer(34);//使用数字来实例化
        Integer n1 = new Integer("100");//使用字符串来实例化
        System.out.println("num:"+num);
        System.out.println("n1:"+n1);

        Integer n2 = 100;//直接用数字
        System.out.println("n2:"+n2);
        //valueof、paraseInt 字符串转整数
        Integer n3 =  Integer.valueOf("100");//将字符串转成整数
        System.out.println("n3:"+n3);
        Integer n4 = Integer.valueOf("FFFFF",16);//radix 表示进制,前面的字符串s是多少进制的数字。
        System.out.println("n4:"+n4);
        Integer n5 = Integer.valueOf("100",16);
        System.out.println("n5:"+n5);
        System.out.println("******************");
        //paraseInt 字符串转整数
        Integer n6 =Integer.parseInt("100");
        int n7 =Integer.parseInt("100",16);
        System.out.println("n6:"+n6);//100
        System.out.println("n7:"+n7);//256

        //基本类型和包装类之间的自动转换：装箱和拆箱
        Integer i = 5;//自动装箱：int类型赋值给Integer类型的变量
        int j = i;//自动拆箱：Integer类型直接赋值给int类型的变量

        //进制：二、八、十、十六
        int b1 = 0b111000;//0b
        int b2 = 0127;//0
        int b3 = 0xAABBAA;//0x
        System.out.println(b1);//56
        System.out.println(b2);//87
        System.out.println(b3);//11189162
        //进制转换
        System.out.println(Integer.toBinaryString(100));//1100100
        System.out.println(Integer.toOctalString(100));//144
        System.out.println(Integer.toHexString(100));//64

        //二、八、十六转为十进制
        System.out.println(Integer.valueOf("11001010",2));//202
        System.out.println(Integer.valueOf("77777",8));//32767
        System.out.println(Integer.valueOf("77777",16));//489335

        //设计10个用例
        System.out.println("*****测试用例*****");
        System.out.println("23456");//正常：范围内的值
        System.out.println(oct2dec("00000"));//正常:最大值
        System.out.println(oct2dec("77777"));//正常：最小值
        System.out.println(oct2dec("1111"));//长度非法：4位
        System.out.println(oct2dec("222222"));//长度非法：6位
        System.out.println(oct2dec("33338"));//数字非法：非8进制
        System.out.println(oct2dec(null));//异常：空值
        System.out.println(oct2dec("+12345"));//正常：去掉符号后，5位，能正常转换
        System.out.println(oct2dec("-54321"));//正常：去掉符号后，5位，能正常转换
        System.out.println(oct2dec("12+34"));//异常：符号位置非法
        // 二进制：0、1
        // 三进制：0、1、2
        // 八进制：0、1、2、3、4、5、6、7
        // 十进制：0、1、2、3、4、5、6、7、8、9
        // 十六进制：0、1、2、3、4、5、6、7、8、9、a、b、c、d、e、f
        // 三十六进制：0~9、a~z


        Float f = +3.14F;
        Float f1 = -3.14F;


    }
    /*
    写一个静态函数，将一个5位的八进制数字转成10进制的
     */
    public static int oct2dec(String oct){
        int flag = 1;
        if (oct == null){
            System.out.println("输入的值不合法");
            return -10001;//返回错误码
        }
        if (oct.charAt(0)=='+'){//单引号
            oct = oct.substring(1);//取字串，从1开始到结束
//            System.out.println("=========="+oct);
        }
        if (oct.charAt(0)=='-'){
            oct = oct.substring(1);
            flag = -1;
        }
        if (oct.length() !=5){
            System.out.println("输入长度不合法");
            return -10002;
        }try{
            return flag * Integer.parseInt(oct,8);//valueOf也可以，parseInt返回基本类型，valueOf返回包装类型
        }catch (Exception e){
            System.out.println("非法的8进制数字");
        }return -10003;

    }
}
