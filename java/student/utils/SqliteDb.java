package student.utils;

import student.model.Student;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/*
数据库的工具类
https://mvnrepository.com/  jar包下载
 */
public class SqliteDb {
    private Connection conn;

    private void connect(){
        try {
            //连接数据库
            Class.forName("org.sqlite.JDBC");
            //连接数据库，返回的连接对象，使用变量存储。
            conn = DriverManager.getConnection("jdbc:sqlite:student.db");
            System.out.println("连接数据库成功");
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("连接数据库失败，异常信息为："+e.getMessage());
        }
    }
    //断开数据库连接
    private void disconnect(){
        try {
            if (conn !=null){
                conn.close();
            }
        }catch (Exception e){
            System.out.println("断开数据库连接异常，异常信息为："+e.getMessage());
        }
    }
    //执行sql语句,增删改类的操作，返回true/false
    private boolean excute(String sql){
        try {
            //连接数据库，相当于建立到数据库之间的一条路
            //Statement 相当于一辆车，将数据从数据库中取出来
            Statement s = conn.createStatement();
            s.execute(sql);
            int count = s.getUpdateCount();//执行sql语句更新了多少条数据
            System.out.println("执行"+sql+"成功，更新了"+count+"条数据");
            return count >=1;//ture
        }catch (Exception e){
            System.out.println("执行"+sql+"语句异常，异常信息为："+e.getMessage());
        }
        return false;
    }
    //执行sql语句，查询类的操作，发挥结果为list<Student>
    private List<Student> executeQuery(String sql){
        List<Student> students = new ArrayList<>();
        try {
            Statement s = conn.createStatement();
            boolean ret = s.execute(sql);
            if (ret == true){
                ResultSet rs = s.getResultSet();
                if (rs !=null){
                    while (rs.next()){
                        String id = rs.getString("id");//"id" 根据列表获取对应的值，放到变量id中
                        String name = rs.getString("name");
                        String gender = rs.getString("gender");
                        String age = rs.getString("age");
                        String phone = rs.getString("phone");
                        String score = rs.getString("score");
                        Student stu = new Student(id,name,age,gender,phone,score);
                        students.add(stu);
                    }
                }
            }
        }catch (Exception e){
            System.out.println("执行"+sql+"语句异常，异常信息为："+e.getMessage());
        }return students;
    }
    //初始化表格
    public static void initTable(){
        SqliteDb db = new SqliteDb();
        db.connect();
        db.excute("create table if not exists student(id varchar(32) primary key,name varchar(32) ,gender varchar(8), age varchar(8),phone varchar(11),score varchar(8));");
        db.disconnect();

    }
    //添加学生
    public static boolean addStudent(Student stu){
        String id = stu.getId();
        String name = stu.getName();
        String age = stu.getAge();
        String gender = stu.getGender();
        String phone = stu.getPhone();
        String score = stu.getScore();
        //insert into student values(id,name,gender,phone,score);
        String sql = "insert into student values('"+
                id + "','"+
                name +"','"+
                age +"','"+
                gender +"','"+
                phone +"','"+
                score +"');";
        SqliteDb db = new SqliteDb();
        db.connect();
        boolean b = db.excute(sql);
        db.disconnect();
        return b;
    }
    //根据名字删除学生
    public static boolean deleteStudent(String name){
        String sql = "delete from student where name ='"+name+"';";
        SqliteDb db = new SqliteDb();
        db.connect();
        boolean b = db.excute(sql);
        db.disconnect();
        return b;
    }
    //修改
    public static boolean modifyStudent(String id,String name,String age,String gender,String phone,String score){
        //update student set 列名1=新值1 where子句；
        String sql = "update student set " ;
        if(!(name == null || name.equals(""))){
            sql+="name = '"+name+"',";
        }
        if(!(age == null || age.equals(""))){
            sql+="age = '"+age+"',";
        }
        if(!(gender == null || gender.equals(""))){
            sql+="gender = '"+gender+"',";
        }
        if(!(phone == null || phone.equals(""))){
            sql+="phone = '"+phone+"',";
        }
        if(!(score == null || score.equals(""))){
            sql+="score = '"+score+"',";
        }
        sql = sql.substring(0,sql.length()-1)+" where id = '"+id+"';";

        SqliteDb db = new SqliteDb();
        db.connect();
        boolean b = db.excute(sql);
        db.disconnect();
        return b;
    }
    //根据名字模糊查询
    public static List<Student> queryStudent(String str){
        String sql = "select * from student where name like '%"+str+"%';";
        SqliteDb db = new SqliteDb();
        db.connect();
        List<Student> students = db.executeQuery(sql);
        db.disconnect();
        return students;
    }
    //全量查询
    public static List<Student> queryStudent(){
        String sql = "select * from student;";
        SqliteDb db = new SqliteDb();
        db.connect();
        List<Student> students = db.executeQuery(sql);
        db.disconnect();
        return students;
    }
    /*
    列表转成二维数组
     */
    public static String[][] list2Array(List<Student> students){
        String[][] result = null;
        if (students.size()>0){//如果列表中有数据，再转成数组。
            result = new String[students.size()][6];
            for (int i =0;i<students.size();i++){
                //从列表中取出一个学生
                Student stu = students.get(i);
                //放到数组中
                //{"编号","名字","年龄","性别","电话","分数"}
                result[i][0] = stu.getId();
                result[i][1] = stu.getName();
                result[i][2] = stu.getAge();
                result[i][3] = stu.getGender();
                result[i][4] = stu.getPhone();
                result[i][5] = stu.getScore();
            }
        }
        return result;
    }


    //测试代码
    public static void main(String[] args) {
//        SqliteDb db = new SqliteDb();
//        db.connect();
//        db.excute("create table if not exists student(id varchar(32) primary key,name varchar(32) ,gender varchar(8), age varchar(8),phone varchar(11),score varchar(8));");
//        db.excute("INSERT INTO STUDENT VALUES('1009','李探花','女','25','13088888888','86');");
//        db.excute("INSERT INTO STUDENT VALUES(\"1001\",\"唐三\",\"男\",\"20\",\"13011112222\",\"90\");");
//        db.excute("INSERT INTO STUDENT VALUES(\"1002\",\"张明\",\"男\",\"20\",\"13022223333\",\"80\");");
//        db.excute("INSERT INTO STUDENT VALUES(\"1005\",\"张三\",\"男\",\"20\",\"13011111111\",\"60\")");
//        db.disconnect();
//        modifyStudent("小三","唐三");
//        deleteStudent("张明");//删除

//        List<Student> ss = SqliteDb.queryStudent("花");//模糊查询
//        System.out.println(ss.toString());
//
//        List<Student> s2 = SqliteDb.queryStudent();//全量
//        System.out.println(s2.toString());


    }

}
