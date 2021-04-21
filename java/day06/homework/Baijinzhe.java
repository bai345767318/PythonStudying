package day06.homework;

/*
作业
 */
public class Baijinzhe {
    public static void main(String[] args) {
        System.out.println(z01("basddb",'b'));

        System.out.println(z02("adassffsdf",5));

        System.out.println(z03("I love China"));

    }

    public static int z01(String s, char c){
        int count = 0;
        for (int i=0;i<s.length();i++){
            if (s.charAt(i) == c){
                count++;
            }
        }
        return count;

    }

    public static String z02(String s,Integer k){
        if (k<s.length()){
            return s.substring(0,k);
        }
        return s.substring(0,k);
    }

    public static String z03(String s){
        String[] a = s.split(" ");
        String c="" ;
        for (int i=a.length-1;i>=0;i--){
            String b = "";
            c = c+a[i]+" ";
        }
        return c;
        }
}







