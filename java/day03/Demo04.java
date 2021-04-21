package day03;

/*
static关键字，修饰方法。
 */
public class Demo04 {
    String name;

    public int add(int a, int b) {
        System.out.println(name);//null 执行顺序？
        return a + b;
    }

    public static int add2(int a, int b) {
        //静态方法不能访问类属性
        //System.out.println(name);
        return a + b;
    }

    public static void main(String[] args) {
        //静态方法，不用实例化，可以直接调用。---属于类
        //使用类名.方法名()调用，如果同一个类内部，类名可以省略。
        System.out.println(add2(5, 20));
        System.out.println(Test.add(20, 15));
        //非静态方法，属于实例，只能实例化后调用。
        Demo04 d = new Demo04();
        System.out.println(d.add(10, 20));
    }
}

class Test {
    public static int add(int a, int b) {
        return a + b;
    }

}