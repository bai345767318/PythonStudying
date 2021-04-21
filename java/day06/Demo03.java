package day06;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/*
文件操作：File
 */
public class Demo03 {
    public static void main(String[] args) throws IOException {
        //相对路径，相对工程的路径
        File file = new File("src/day06/test.txt");
        boolean isTrue = file.createNewFile();//创建文件
        System.out.println("创建文件是否成功:"+isTrue);//true

        //判断是文件还是目录
        System.out.println("file.isDirectory():"+file.isDirectory());//false
        //文件存在返回true
        System.out.println("file.isFile():"+file.isFile());//true
        File path = new File("C:\\Program Files\\Java\\jdk-12.0.1\\bin");
        //目录存在返回true，否则false
        System.out.println("path.isDirectory():"+path.isDirectory());//true

        isTrue =  file.delete();//删除文件
        System.out.println("删除文件是否成功："+isTrue);//true

        File p = new File("D:\\learnjava");
        //列出目录下的所有目录/文件
        String[] fs = p.list();
        for (String f:fs){
            System.out.println(f);
        }

        File[] ffs = p.listFiles();
        for (File f:ffs){
            System.out.println(f.getAbsolutePath());//获取绝对路径
        }
        System.out.println("************分割线************");
        List<File> files = getAllFile("D:\\learnjava");
        for (File f:files){
            System.out.println(f.getAbsolutePath());
        }
        System.out.println("**************分割线***************");

    }
        /*
        练习：获取目录以及子目录下所有java文件，放到List中
         */
        public static List<File> getAllFile(String path){
            List<File> allFiles = new ArrayList<>();//定义一个列表存储结果
            File file =new File(path);
            if (file.isDirectory()){//如果是目录，获取下面的文件列表
                File[] fs = file.listFiles();
                for (File f:fs){
                    //递归
                    //把一个列表加入到另一个列表，使用addAll
                    allFiles.addAll(getAllFile(f.getAbsolutePath()));//添加列表到allFiles这个列表中
                }
            }else if (file.isFile()){//如果是文件
                //获取后缀
                String houzhui = path.substring(path.lastIndexOf(".")+1);
                //如果后缀是java，加入到存放结果的列表中
                if (houzhui.equalsIgnoreCase("java")){
                    allFiles.add(file);
                }
            }
            else {//既不是目录又不是文件
                System.out.println("输入的路径不正确");
            }
            return allFiles;
        }

}
