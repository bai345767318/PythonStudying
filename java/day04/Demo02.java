package day04;
/*
继承：
继承使用extends关键字。继承了父类的属性和方法，不继承父类的构造方法
python可以有多个父类;
java支持单继承和多层继承(子类->父类->祖父->曾祖父 节点)，不支持多个父类.--间接继承
所有类的父类是Object。
 */
public class Demo02 {
    public static void main(String[] args) {
        Pet dog = new Pet("步枪",5,64);
//        dog.setAge(5);
//        dog.setName("步枪");
//        dog.getHealth(64);
        System.out.println(dog.toString());

        Pet cat = new Pet("小米",-4,70);
//        cat.setName("小米");
//        cat.setAge(-4);
//        cat.getHealth(70);
        System.out.println(cat.toString());

        Dog d1 =new Dog("旺财",10,90,"拉布拉多");
        d1.setHealth(80);//子类可以直接使用父类中定义的方法
        System.out.println(d1.toString());

    }
}
class Dog extends Pet{
    private String pinzhong;//宠物狗相对Pet类来说特有的属性。

    public String pinzhong(){
        return pinzhong;
    }
    public void setPinzhong(String pinzhong){
        this.pinzhong = pinzhong;
    }

    public Dog(String name,int age,int health,String pinzhong){
        //调用父类的构造方法。
        super(name,age,health);//super 是父类的意思，superclass 父类也叫超类。
        this.pinzhong = pinzhong;
    }
    //子类重写父类的toString方法。
    public String toString(){
        return "宠物狗,品种:"+pinzhong+",名字："+super.getName()+",年龄:"
                +super.getAge()+" 健康度:"+super.getHealth();
    }   

}
/*
新建一个宠物类
类名：Pet
属性：name age  health(取值范围：0-100)，设置成私有的
方法：每个属性get/set方法，构造方法，toString方法
 */

class Pet{
    private String  name;
    private int age;
    private int health;

    public Pet(String name,int age,int health){
        this.name = name;
        this.setAge(age);
        this.health = health;
//        this.setHealth(health);
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age>=0){
            this.age = age;
        }
        else {
            System.out.println("请设置合法年龄");
        }
    }
    public int getHealth(){
         return health;
    }
    public void setHealth(int health){
        if (health >= 0 && health <= 100) {
            this.health = health;
        }else {
            System.out.println("请设置合理健康度(0-100)");
        }
    }
    @Override
    public String toString() {
        return "Pet{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", health=" + health +
                '}';
    }


}
/*
练习：
圆的类：Circle
    属性 r
    方法：
    周长、面积
圆柱的类：从圆继承 Cylinder
    属性：h
    方法：表面积(重写父类的面积方法)
 */
class Circle{
    private double r;
    public Circle(double r) {
        this.r = r;
    }

    public double getR() {
        return r;
    }

    public void setR(double r) {
        this.r = r;
    }
    //周长
    public double getZc(){
        return 2*Math.PI*r;
    }
    //面积
    public double getMj(){
        return Math.PI*r*r;
    }

}

class Cylinder extends Circle{
    private double h;
    public  Cylinder(double r,double h){
        super(r);//父类的构造方法
        this.h=h;
    }

    public double getH() {
        return h;
    }

    public void setH(double h) {
        this.h = h;
    }
    //表面积：2πrh+2πrr
    public double surface_area(double r, double h){
        return  2*Math.PI*r*h+2*Math.PI*r*r;

    }
    //体积：πrrh
    public double volume(double r,double h){
//        return Math.PI*r*r*h;
        return super.getMj()*h;//父类获取面积的方法
    }

    @Override
    public String toString() {
        return "Cylinder{r=" +super.getR()+";h=" + h +'}';
    }

    public static void main(String[] args) {
        Cylinder c1 = new Cylinder(2,3);
        System.out.println(c1.surface_area(2,3));
        System.out.println(c1.volume(2,3));
        System.out.println(c1.toString());
    }

}
