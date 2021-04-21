package day06;

import java.io.*;

/*
写文件：从内存中写到磁盘
1.按字节。FileOutputWriter
2.按字符。OutputStreamWriter,FileWriter
3.按行。BufferedWriter
 */
public class Demo05 {
    public static void main(String[] args) throws IOException {
        String content  = "君不见黄河之水天煞过来，奔流到海不复回;\n"+
                "君不见高堂明镜悲白发，朝如青丝暮成雪。\n";
        write1("src/day06/test1.txt",content);
        write2("src/day06/test2.txt",content);
        write3("src/day06/test3.txt",content);

    }
    //写文件
    //按字节写
    public static void write1(String fileName,String content) throws IOException {
        //如果是true，表示追加，否则是覆盖写。
        FileOutputStream fos = new FileOutputStream(fileName,true);
        byte[] bytes = content.getBytes();//字符串转换成byte数组
        fos.write(bytes);
        fos.close();
    }
    //按字符写
    public static void write2(String fileName,String content) throws IOException {
        //FileWriter
        //BufferedWriter
        //1.创建一个对象，看构造方法需要什么参数，传相应的参数
        //2.使用write写文件，看write需要什么参数，传相应的参数
        //3.关闭文件
        FileWriter fw = new FileWriter(fileName,true);
        fw.write(content);
        fw.close();
    }
    //按行写
    public static void write3(String fileName,String content) throws IOException {
        FileWriter fw = new FileWriter(fileName,true);
        BufferedWriter bw = new BufferedWriter(fw);
        bw.write(content);
        bw.close();
    }

}
