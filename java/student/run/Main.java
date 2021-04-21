package student.run;

import student.utils.SqliteDb;
import student.view.MainView;

/*
程序入口
 */
public class Main {
    public static void main(String[] args) {
        //1.创建数据库，初始化表格
        SqliteDb.initTable();
        //2.创建主页面
        new MainView();
    }
}
