package day05;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

/*
Map:类似Python种的字典，key、value的方式存放数据。
Map是接口，HashMap是使用比较多的实现。
    put(增/改)、get、remove、keyset(获取所有key)
 */
public class Demo05 {
    public static void main(String[] args) {
        //<String,String> 前面是key的类型，后面是value的类型
        Map<String,String> map = new HashMap<>();

        //添加/修改元素
        map.put("CNY","人民币");
        map.put("USD","美元");
        map.put("JPY","日元");
        map.put("HKD","港币");
        map.put("USD","美元");//修改
        System.out.println(map);
        System.out.println(map.get("CNY"));//根据key获取value
        map.remove("JPY");//删除元素
        System.out.println(map);
        //遍历字典
        //key唯一，set存储key--去重
        //map.keySet() 获取所有的key
        Set<String> keySet = map.keySet();
        System.out.println(keySet);
        for (String k:keySet){
            System.out.println(k+" "+map.get(k));
        }


        count("aaacaaaaaaaa.aaabdbfb");



    }
    /*
    传入一个字符串，统计字符串中每个字符出现的次数
     */
    public static void count(String s){
        Map<Character,Integer> res = new HashMap<>();
        //遍历字符串
        for (int i=0;i<s.length();i++){
            char ch = s.charAt(i);//根据索引获取每个字符
            //如果字符在map中存在，取出value，给value+，再设置回去
            //map['a'], == >map['a'],2
            //如果字符再map不存在，设置value为1
            //map['a'],1
            if (res.get(ch) != null){
                int value = res.get(ch)+1;
                res.put(ch,value);
            }else {
                //如果字符在map不存在，设置value为1
                //map['a'],1
                res.put(ch,1);
            }
        }
        System.out.println(res);
    }

}
