package day05;
/*
异常处理：
java：try-catch-finaly-throw-throws
 */
public class Demo01 {
    public static void main(String[] args) {
        //java.lang.ArithmeticException: / by zero
        try {
            int num = 10/0;
        }catch (Exception e){//把捕获的异常放到变量e中，e是exception类型大的
            System.out.println(e.getMessage());
            e.getStackTrace();//打印异常的调用栈，也就是函数的调用关系
        }finally {
            System.out.println("程序执行结束");
        }

        //NullPointerException 是代码逻辑错误导致，最好不用try-catch来隐藏这种错误。
        String s = null;//没有赋值，默认null
//        System.out.println(s.equals(""));//java.lang.NullPointerException 空指针
        if (s !=null){
            System.out.println(s.toLowerCase());//转小写
        }
        Person p = new Person("A",10);
        try{
            //如果一个方法抛出了异常，那么
            //1.try-catch捕捉异常
            //2.使用throws声明抛出了一个异常
            p.setAge(130);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}


class Person{
    private String name;
    private int age;

    public Person(String name,int age){
        this.name =name;
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) throws Exception {
        if (age>0&&age<100){
            this.age = age;}
        else
            {throw new Exception("输入合法数字");//抛出一个自定义的异常
        }
    }
}





