package day06;

import javax.sound.sampled.AudioFormat;
import java.io.*;

/*
读写文件：从硬盘读取到内存中  //stream:流
1.按字节读取文件，一次性读以一个字节。FileInputStream
2.按字符读取文件，一次读一个字符。InputStreamReader、FileReader
3.按行读取文件，一次读一行。BufferedReader
 */
public class Demo04 {
    public static void main(String[] args) throws IOException {
        String fileName = "D:\\learnjava\\src\\day06\\Demo03.java";
        System.out.println("readByByte******start*****");
        readByByte(fileName);
        System.out.println("readByChar*******start*****");
        readByChar(fileName);
        System.out.println("readByLine*******start******");
        readByLine(fileName);
        System.out.println("============================");
        //readByByte("C:\\Users\\86177\\Desktop\\bizhi.jfif");//读图片--乱码

    }

    //按字节读取
    public static void readByByte(String fileName) throws IOException {
        FileInputStream in = new FileInputStream(fileName);
        int temp = in.read();//一个字节,-1~255之间的整数
        while (temp !=-1){
            System.out.write(temp);//打印字节用write
            temp = in.read();
        }
        in.close();

    }

    //按字符读取
    public static void readByChar(String fileName) throws IOException {
        FileReader fr = new FileReader(fileName);
        int temp = fr.read();//一次性读一个字符，取值-1~65535；
        while (temp !=-1){//是否达到文件末尾
            System.out.print((char)temp);//把整数转成字符再打印
            temp = fr.read();
        }
        fr.close();//关闭文件
    }

    //按行读取
    public static void readByLine(String fileName) throws IOException {
        //Reader是抽象类，不能实例化，使用它的子类比如FileReader、InputStreamException来实例化
        Reader r = new FileReader(fileName);
        BufferedReader br = new BufferedReader(r);//构造函数需要Reader类型的参数

        String str = br.readLine();//读取一行
        while (str !=null){
            System.out.println(str);
            str = br.readLine();
        }br.close();//关闭
        r.close();
    }


}
