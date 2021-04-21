package day05;

import java.util.HashSet;
import java.util.Set;

/*
set:不允许包含重复的元素。Set 接口，HashSet是实现类，Hash算法来存储元素。
    add()、remove()
 */
public class Demo04 {
    public static void main(String[] args) {
        Set<Float> set = new HashSet<>();

        set.add(1.0F);
        set.add(2.5F);
        set.add(3.0F);
        System.out.println(set);
        set.add(1.0F);//重复元素添加不进去
        System.out.println(set);
        set.remove(1.0F);//删除元素
        System.out.println(set);
        //没有get、set方法，列表中通过索引修改set/获取get元素，set是无序的，没有索引
        //遍历索引
        for (Float f : set) {
            System.out.println(f);
        }
    }
}
