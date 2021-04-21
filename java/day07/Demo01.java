package day07;

public class Demo01 {
    public static int z01(String s, char c){
        int count = 0;
        for (int i=0;i<s.length();i++){
            if (s.charAt(i) == c){
                count++;
            }
        }
        return count;

    }

    public static String jieQu(String str, int k) {
        if(str == null){
            return "ERROR:空值";
        }
        if(k<0||k>=str.length()){
            return "ERROR:索引错误";
        }
        return str.substring(0,k);
    }

    public static String nixu(String str){
        if(str == null) {
            return "ERROR:空值";
        }
        String[] temps = str.split(" ");
        StringBuilder ret = new StringBuilder();
        for(int i = temps.length-1;i>=0;i--){
            if(i == 0){
                ret.append(temps[i]);
            }else {
                ret.append(temps[i]).append(" ");
            }
        }
        return ret.toString();
    }
    public static String isTriangle(int a,int b,int c){
        if (a<=0 || b<=0 ||c<=0){
            return "Error:参数错误";
        }
        if (!(a+b>c && a+c>b && b+c>a)){
            return "不是三角形";
        }else if (a==b && a==c){
            return "等边三角形";
        }else if (a==b || a==c || b==c){
            return "等腰三角形";
        }else {
            return "一般三角形";
        }
    }

}
