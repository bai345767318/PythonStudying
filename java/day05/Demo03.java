package day05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
列表、集合、Map(字典)
pyhton集合：无序、不能重复、可变长度、可以包含任意类型的元素
python；列表：有序、可变长度、可以包含任意类型的元素

java 列表：list：有序、可重复、可变长度，但是只能是某一个类型的。
        ArrayList：可变长度的数组。
        LinkedList:链表方式存储数据。插入、删除元素效率比较高。长度不可变。
 */
public class Demo03 {
    public static void main(String[] args) {
        //list是接口，不能实例化，ArrayList、LinkedList是典型的实现类
        //<Integer> 表示列表种的元素是Integer类型的。int报错。
        //List<int> list1 = new ArrayList();
        List<Integer> list = new ArrayList();
//        List<Integer> list2 = new Arrays.asList(1,3,5,7,9);//报错
        //增删改查 add、set、remove
        list.add(1);//添加元素
        list.add(2);
        list.add(5);


        list.set(0,3);//修改元素：索引,值,只能修改列表中有的
//        list.set(5,10);//IndexOutOfBoundsException
        System.out.println(list);
        System.out.println(list.get(0));//获取元素
//        System.out.println(list[0]);//列表不支持
        list.remove(1);//删除索引对应的元素
        Integer a = 5;
        System.out.println(list);
        list.remove(a);//删除某个元素
        System.out.println(list);

        List<String> names = new ArrayList<>();//将数组转换为列表list
        names.add("A");
        names.add("B");
        names.add("C");
        System.out.println(names);
        names.remove(1);//删除索引对应的元素
        names.remove("D");//删除某个元素
        System.out.println(names);

        List<String> names2 = new ArrayList<>(Arrays.asList("A","B","C"));

        System.out.println(names2);
//        names2.remove("A");//Arrays.asList,不能使用索引删除

        //for遍历列表、foreach遍历列表
        for (int i=0;i<list.size();i++){
            System.out.println(list.get(i));
        }
        for (String s : names2) {
            System.out.println(s);
        }
        /*
        新建一个class Person,名字，年龄
        创建5个Person，把Person放入列表
                */
        List<Person> persons = new ArrayList<>();
        for (int i=0;i<5;i++){
            Person p1 = new Person("name"+i,10+i);
            persons.add(p1);
            System.out.println(p1.toString());
        }



    }

}