package day04;

/*
面向对象三大特征
封装：把属性编程私有的，提供set/get方法访问
继承：
多态：
函数的封装和调用
 */
public class Demo01 {
    public static void main(String[] args) {
        Student xiaoHua = new Student();
        xiaoHua.name = "小花";//实例.属性，设置属性的值
        xiaoHua.age = 18;
        xiaoHua.gender = "女";
        System.out.println(xiaoHua.name);//获取属性的值
        System.out.println(xiaoHua.toString());

        Student1 xiaoMei = new Student1();
//        xiaoMei.name = "";//私有属性，类外部无法访问
        xiaoMei.setName("小美");//设置属性的值
        System.out.println(xiaoMei.getName());
        System.out.println(xiaoMei.toString());
        xiaoMei.setGender("女");
        System.out.println(xiaoMei.toString());
        xiaoMei.setGender("鬼");//设置非法的值，
        System.out.println(xiaoMei.toString());
        xiaoMei.getGender();
        System.out.println(xiaoMei.toString());
        xiaoMei.setAge(-1);//设置非法年龄
        System.out.println(xiaoMei.toString());


    }
}

class Student {
    String name;
    int age;
    String gender;

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", gender='" + gender + '\'' +
                '}';
    }
}

class Student1 {
    //使用private修饰，只能在类的内部访问。
    private String name;
    private int age;
    private String gender;

    //set方法，获取属性的值
    public void setName(String n) {
        name = n;
    }

    //get方法
    public String getName() {
        return name;
    }

    public void setAge(int a) {
        if (age > 0) {
            age = a;
        } else {
            System.out.println("请输入正确的年龄");
        }
    }

    public int getAge() {
        return age;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String g) {
        if (g.equals("男") || g.equals("女")) {
            gender = g;
        } else {
            System.out.println("参数输入错误，请输入男/女");
        }
    }

    @Override
    public String toString() {
        return "Stdent1{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", gender='" + gender + '\'' +
                '}';
    }
}

class Student2 {
    //私有
    private String name;
    private int age;
    private String gender;

    //get/set可以自动生成
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
}