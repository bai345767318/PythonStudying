package day02;

import java.lang.reflect.Array;
import java.util.Arrays;

/*
数组：相同类型的一组数据，使用一个名字命名。
类似列表
 */
public class Demo02 {
    public static void main(String[] args) {
        //学生学号的数组
        //int[] 表示int类型的数组。
        //声明了一个数组，并对数组进行初始化
        //初始化完成后，长度就固定了
        int[] ids = new int[]{1001, 1002, 1003, 1004};
        System.out.println(ids[0]);
        System.out.println(ids[3]);//不支持-1
        //System.out.println(ids[4]);//ArrayIndexOutOfBoundsException

        int ids2[] = new int[10];//声明一个数组 长度是10
        ids2[0] = 1001;//初始化
        ids2[1] = 1002;
        System.out.println(ids2[0]);

        int[] ids3 = {1001, 1002, 1003, 1004};//通过值能推断类型，可以省略 new int[]
        //取数组的长度
        System.out.println(ids3.length);
        //遍历数组：for循环，遍历的是索引
        for (int i = 0; i < ids3.length; i++) {
            System.out.println(ids[i]);
        }
        //遍历数组:foreach遍历，遍历的是值，每次取出一个元素。
        for (int value : ids3) {
            System.out.println(value);
        }
        //定义一个字符串类型的数组，存放人名，数组名字：names
//        String[] names = new String[5];
        String[] names = {"春", "夏", "秋", "冬"};
        //for
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }
        System.out.println();
//        //foreach
        for (String name : names) {
            System.out.println(name);
        }
        //数组不初始化时，会有默认值。基本类型的数组，默认值是对应类型的0值。
        //String 引用类型，默认值是null。引用类型也就是使用class定义的类型。
        float[] f = new float[5];
        for (float a : f) {
            System.out.println(a);//0.0
        }
        String[] classes = new String[10];
        for (String s : classes) {
            System.out.println(s);//null
        }
        //数组的应用:取数组中的最大值/最小值大
        // 打擂的方式，max,先把第一个元素赋值给max，后面的元素跟max比，如果比max大，将max替换。
        int[] nums = {9, 8, 12, 1, 3, 6, 44, 67};
        //取最大值
        int max = nums[0];
        int min = nums[0];
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
            if (min > num) {
                min = num;
            }
        }
        System.out.println(max);
        System.out.println(min);
        //对nums进行冒泡排序
        System.out.println("排序之前:" + Arrays.toString(nums));//数组转字符串
        for (int i = 0; i < nums.length; i++) {//轮次
            for (int j = 0; j < nums.length - i - 1; j++) {//比较次数
                if (nums[j] > nums[j + 1]) {
                    //定义一个临时变量，交换两个变量的值
                    int temp;
                    temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }

            }
        }
        System.out.println("排序之后:" + Arrays.toString(nums));

        System.out.println(nums);//打印数组的内存地址，在内存中起始的位置。

        int[] scores = {9, 8, 12, 1, 3, 6, 44, 67};
        System.out.println("排序之前:" + Arrays.toString(scores));
        Arrays.sort(scores);//排序-升序
        System.out.println("排序之后:" + Arrays.toString(scores));

        //binarySearch 第一个参数是一个升序的数组
        int ret = Arrays.binarySearch(scores, 12);//二分查找
        System.out.println(ret);//5如果存在，返回索引。
        int r = Arrays.binarySearch(scores, 13);
        System.out.println(r);//不存在时，返回-(插入点+1) -(6+1)
        r = Arrays.binarySearch(scores, 0);
        System.out.println(r);//-1
        //[1, 3, 6, 8, 9, 12, 44, 67]
        //要找3：第一次：9，第二次：6，第三次：3

        int[] arr1 = {10, 20, 30};
        int[] arr2 = {10, 20, 30};
        int[] arr3 = {10, 20, 30};
        System.out.println(Arrays.equals(arr1, arr2));//比较两个数组中的元素是否相等
        System.out.println(Arrays.equals(arr1, arr3));
        System.out.println(arr1);
        System.out.println(arr2);
        System.out.println(arr1 == arr2);//比较的是内存地址，不能用==来判断两个数组的值



    }
}
