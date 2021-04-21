package day06;

import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.StringJoiner;

/*
String:字符串
 */
public class Demo02 {
    public static void main(String[] args) {
        String s1 = "Hello World";

        System.out.println(s1.length());//长度
        System.out.println(s1.charAt(0));//根据索引获取对应字符，类似Python中的s1[0]
        //取字串
        System.out.println(s1.substring(6));//一个参数时，表示开始索引
        System.out.println(s1.substring(0,5));//两个参数时，表示开始和结束，包含开始，不包含结束。

        System.out.println(s1.indexOf(" "));//获取字符在字符串中的位置/索引
        s1 = "Hello World Hello World";
        System.out.println(s1.indexOf(" "));//如果有多个字符，只返回第一个位置
        System.out.println(s1.lastIndexOf(" "));//最后一个空格所在的位置

        //练习：
        //文件路径，取到文件的后缀名
        //E:\\test\\src\\day06\\demo01.java  //后缀名：java
        //D:\\test\\hello.world.xml  //后缀名:xml
        String s2 = "E:\\test\\src\\day06\\demo01.java;";
        String s3 = "D:\\test\\hello.world.xml";
        System.out.println(s2.indexOf("."));
        System.out.println(s3.lastIndexOf("."));
        System.out.println(s2.substring(25,29));
        System.out.println(s3.substring(20,23));
//        System.out.println(s2.substring(s2.lastIndexOf(".")+1));

        //分隔字符串，用\\分隔是字符串
        String[] temp = s2.split("\\\\");
        System.out.println(Arrays.toString(temp));
        //获取数组中最后一个元素，最后一个元素的索引是：长度-1
        System.out.println(temp[temp.length-1]);//获取文件名
        //拼接字符串,第一个参数是用什么连接，后面是可变个参数，要连接的字符串。
        String s4 = String.join("/","D:","test","src","day06","demo01.java");
        System.out.println("s4:"+s4);

        String str1 = "123";
        String str2 = "456";
        String str3 = str1+str2;//拼接用加法
        System.out.println(str3);
        str3 = str1.concat(str2);//拼接用concat
        System.out.println(str3);
        //大量字符串拼接时，效率低，耗时久
        String s = "";
        long begin = (new Date()).getTime();
        for (int i=0;i<10000;i++){
            s = s+i+",";
        }
        long end = (new Date()).getTime();
//        System.out.println(s);
        System.out.println("拼接耗时："+(end-begin)+"毫秒");

        //使用StringBuilder拼接字符串，效率较高
        StringBuilder sb = new StringBuilder();
        begin = (new Date()).getTime();
        for (int i=0;i<10000;i++){
            sb.append(i);
            sb.append(",");
        }end = (new Date()).getTime();
//        System.out.println(sb);
        System.out.println("拼接耗时："+(end-begin)+"毫秒");

        /*
        练习：效果：Hello Bob，Alice，Lily!
         */
        List<String> names = Arrays.asList("Bob","Alice","Lily");
        //方法1 使用StringBuilder拼接
        StringBuilder sn = new StringBuilder();
        sn.append("Hello ");
        for (int i =0;i<names.size();i++) {
            sn.append(names.get(i));
            if (i == names.size()-1){//如果是最后一个，加！号
                sn.append("!");
            }else {
                sn.append(", ");//如果不是最后一个,加,号
            }

        }
        System.out.println(sn);

        //方法2 使用StringBuilder拼接
        sn = new StringBuilder();
        sn.append("Hello ");
        for (String name:names) {
            sn.append(name).append(", ");//多拼了个逗号和空格
        }
        //Hello Bob,Alice,Lily,  逗号是倒数第二个字符，索引的length-2
        sn.delete(sn.length()-2,sn.length());//delete包含开始的索引，不包含结束的索引
        sn.append("!");
        System.out.println(sn);

        //方法3：使用join
        String s5 = String.join(", ",names);
        System.out.println("Hello "+s5+"!");
        //方法4：StringJoiner 专门用来拼接字符串的类   分隔字符       前缀     后缀
        StringJoiner sj = new StringJoiner(", ","Hello ","!");
        for (String name:names){
            sj.add(name);
        }
        System.out.println(sj);
        //字符串判等
        String a = "123a";
        String b = new String("123a");
        String c = "123a";
        String d = "123A";
        System.out.println(a==b);//false ==判断的是内存地址
        System.out.println(a==c);//true ==判断的是内存地址
        System.out.println(a.equals(b));//判断字符串是否相等true
        System.out.println(a.equals(d));//false
        System.out.println(a.equalsIgnoreCase(d));//判断字符串是否i相等，不区分大小写，true
    }

}
