package day05;

import java.util.*;

/*
集合的工具类：Collections 搜集、收藏,提供了一些操作列表的方法，比如查找、排序、最大值、最小值
 */
public class Demo06 {
    public static void main(String[] args) {
        List<String> cs = new ArrayList<>();
        cs.add("red");
        cs.add("yellow");
        cs.add("black");
        cs.add("green");
        cs.add("yes");
        cs.add("11");


        System.out.println(cs);
        Collections.sort(cs);//排序，从小到大升序排列，按ASCII码
        System.out.println(cs);
        System.out.println(Collections.max(cs));
        System.out.println(Collections.min(cs));

        Collections.reverse(cs);//翻转列表
        System.out.println(cs);
        //二分查找：cs 升序的序列。
        Collections.reverse(cs);
        System.out.println(cs);
        int n = Collections.binarySearch(cs, "yes");
        System.out.println(n);


        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        qiepian(list, -1, 3);//报错
        qiepian(list, 0, 5);//报错
        qiepian(list, 3, 2);//报错
        System.out.println(qiepian(list, 1, 4));//

    }

/*
定义一个静态方法，3个参数，第一个参数是列表，第二个参数是起始的下标，第三个是结束的下标。
返回列表中包含起始，和结束下标之间的子列表。
[1,2,3,4,5],1,3 =>[2,3,4]
类似python中的切片功能。
 */
    public static List<Integer> qiepian(List<Integer> list, int start, int end) {
        if (start < 0 || end >= list.size() || end < start) {
            System.out.println("索引错误");
            return null;
        }
        List<Integer> result = new ArrayList<>();
        for (int i = start; i <= end; i++) {
            result.add(list.get(i));
        }
        return result;
    }


}



