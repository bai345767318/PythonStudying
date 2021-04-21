package day04;
/*
多态：把子类的对象当作父类的对象来使用
 */
public class Demo03 {
    //给宠物看病的方法
    public static void master(Pet pet){
        if (pet.getHealth()<60){
            System.out.println("吃药打针");
            pet.setHealth(pet.getHealth()+10);
        }else {
            System.out.println("洗澡按摩");
            pet.setHealth(pet.getHealth()+5);
        }
    }
    public void dogMaster(Dog dog){//非static，调用时需要先实例化
        if (dog.getHealth()<60){
            System.out.println("吃药打针");
            dog.setHealth(dog.getHealth()+10);
        }else {
            System.out.println("洗澡按摩");
            dog.setHealth(dog.getHealth()+5);
        }
    }
    public static void main(String[] args) {//static,调用时不用实例化
        Dog d = new Dog("小黑",10,60,"狼狗");
        System.out.println(d.toString());
        master(d);//master可以传入Pet以及Pet的子类。
        Demo03 demo03 = new Demo03();//
        demo03.dogMaster(d);//dogMaster可以传入Dog以及Dog的子类
        System.out.println(d.toString());

        //rd可以当作RedDog、Dog、Pet类型来使用。-----多态。
        RedDog rd = new RedDog("小红",2,50,"红毛犬");
        System.out.println(rd.toString());
        master(rd);//master可以传入Pet以及Pet的子类。
        System.out.println(rd.toString());

        //pet
        Pet p = new Pet("仓鼠",1,50);
        System.out.println(p.toString());
        master(p);
//        demo03.dogMaster(p);//Pet不能作为Dog来使用，Dog能作为Pet来使用。
        System.out.println(p.toString());


    }
}

class RedDog extends Dog{

    public RedDog(String name,int age,int health,String pinzhong){
        super(name, age, health, pinzhong);
    }
}
