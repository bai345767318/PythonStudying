package student.view;

import student.model.Student;
import student.utils.SqliteDb;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;

//主页面，从JFrame继承
//java-swing分了3层：顶层容器：JFrame，中间层容器：JPanel，组件：文本框、标签、按钮等等
public class MainView extends JFrame {
    public static JTextField condition;//将下面48行局部变量变成属性,之前是私有，不能访问，变成属性后能够访问
    public static JTable jTable;//将下面65行局部变量变成属性,之前是私有，不能访问，变成属性后能够访问

    //构造方法，在这里绘制界面
    public  MainView(){
        JPanel n = northPanel();
        JPanel c = centerPanel();
        //将JPanel加到JFrame上，并设置好方位。
        this.add(n, BorderLayout.NORTH);
        this.add(c,BorderLayout.CENTER);

        //设置JFrame的一些属性
        setTitle("学生管理系统");//标题
        setBounds(400,200,1200,600);//位置、大小
        //显示窗口
        setVisible(true);

    }
    //北面
    private JPanel northPanel(){
        JPanel north = new JPanel();
        //网格布局管理器,一个网格中放一个组件，1行5列，共能放置5个组件。
        GridLayout grid = new GridLayout(1,5);
        north.setLayout(grid);//设置JPanel使用这个布局管理器

        JButton add = new JButton("添加");
        north.add(add);
        //add按钮的监听事件
        add.addActionListener(new AddAction());

        JButton modify = new JButton("修改");
        north.add(modify);
        modify.addActionListener(new ModifyAction());//--

        JButton delete = new JButton("删除");
        north.add(delete);
        delete.addActionListener(new DelectAction());//---
        //文本框,输入的搜索内容，用一个文本框来实现
        condition = new JTextField();
        north.add(condition);

        JButton find = new JButton("查找");
        north.add(find);
        //给按钮增加监听事件
        find.addActionListener(new FindAction());

        return north;
    }
    //中间
    private JPanel centerPanel(){
        JPanel center = new JPanel();
        center.setLayout(new GridLayout(1,1));
        //表格
        jTable = new JTable();
        //表格中单元格的属性
        DefaultTableCellRenderer cr = new DefaultTableCellRenderer();
        //单元格中内容居中对齐
        cr.setHorizontalAlignment(JLabel.CENTER);
        //将单元格属性与表格关联起来
        jTable.setDefaultRenderer(Object.class,cr);// Renderer 渲染器
        //初始化表格，给表格填充数据
        initTable(jTable, SqliteDb.queryStudent());

        //添加一个滚动面板，支持水平和垂直的滚动条
        JScrollPane jScrollPane = new JScrollPane(jTable);
        center.add(jScrollPane);

        //不加滚动面板显示
//        center.add(jTable);

        return center;
    }
    //初始化表格
    //java.util.List 、java.awt.List 两个包中都有List类，避免冲突，可以把包名加上。
    public static void initTable(JTable jTable, java.util.List<Student> students){
        //获取表格的控制模型，返回的是TableModel
        //TableModel是接口，强转成他的一个实现类DefaultTableModel
         DefaultTableModel dt = (DefaultTableModel)jTable.getModel();
          String[][] s = SqliteDb.list2Array(students);
          String[] colunms = {"编号","名字","年龄","性别","电话","分数"};
         //填充数据
        //二维数组存数据，一维数组存表头
        dt.setDataVector(s,colunms);//Vector 载体

    }
    //"添加"按钮的功能
    private class AddAction implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            //点击按钮时，弹出来一个窗口，窗口里面设置学生的相关参数。
            new AddView();
        }
    }
    //查找按钮的功能
    private class FindAction implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            //获取输入框的内容
            String p = condition.getText();
            //查询
            java.util.List<Student> students;
            //如果输入的为空，查询所有
            if (p == null || p.equals("")){
                students = SqliteDb.queryStudent();
            }else {
                //如果有输入，根据名字查询
                students = SqliteDb.queryStudent(p);
            }
            //刷新表格
            initTable(jTable,students);
            //清空搜索框
            condition.setText("");
        }
    }
    //删除选中行
    private class DelectAction implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e) {
            int[] selectedRow = jTable.getSelectedRows();
//            System.out.println(Arrays.toString(selectedRow));
            for (int i = selectedRow.length-1;i>=0;i--){
//                System.out.println(jTable.getValueAt(selectedRow[i],1));
                String name = (String)jTable.getValueAt(selectedRow[i],1);
                boolean b = SqliteDb.deleteStudent(name);
                if (b){
                    JOptionPane.showMessageDialog(null,"删除"+name+"成功！");
                    //刷新表格
                    MainView.initTable(MainView.jTable,SqliteDb.queryStudent());
                }else {
                    JOptionPane.showMessageDialog(null,"删除"+name+"失败");
                }

            }
        }
    }
    //修改选中行
    private class ModifyAction implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
           new ModifyView();
                }
            }


}



