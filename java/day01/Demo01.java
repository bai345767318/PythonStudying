package day01;

/*
class 创建了一个类，类名Demo01，类名首字母大写
public：公共的
java执行时，先编译再运行，编译生成.class文件。
*/
public class Demo01 {
    /*
    main 方法：程序的入口
    public表示是公共的方法
    static表示静态的方法
    void是返回值，表示返回为空
    String[] 表示参数的类型，字符串数组
    args 参数名
    */

    /**
     * 文档注释，可以导出生成一个帮助文档
     * @param args
     */
    public static void main(String[] args) {
        /*
        print line 打印一句话并换行
        每个语句使用;结尾。
        */
        System.out.println("Hello World");
        System.out.print("aaa");
        System.out.print("bbb");
    }
}
//单行注释
/*
多行注释
 */
/*
* 标识符
* 自己起名的地方都是标识符。类名、变量名、方法名
* 命名规则：
*       不能使用数字开头
*       数字、字母、下划线、$组成
*       不能使用Java关键字
* 包名：全小写字母组成
* 类名：大驼峰 XxxYyyZzz
* 变量名、方法名：小驼峰，xxxYyyyZzzz
* 常量：大写字母+下划线组成
* */
