package student.view;

import student.model.Student;
import student.utils.SqliteDb;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.UUID;

public class AddView extends JFrame {
    private JTextField name,age,gender,phone,score;

    public AddView(){
        this.add(northPanel(), BorderLayout.NORTH);
        this.add(southPanel(),BorderLayout.SOUTH);

        setTitle("添加学生");
        setBounds(650,300,500,300);
        setVisible(true);

    }

    private JPanel northPanel(){
        JPanel north = new JPanel();
        GridLayout grid = new GridLayout(5,2);//id让其自动生成
        north.setLayout(grid);

        //新建一个标签，放到中间容器中--对应的文本框
        north.add(new JLabel("姓名"));
        name = new JTextField();
        north.add(name);

        north.add(new JLabel("年龄"));
        age = new JTextField();
        north.add(age);

        north.add(new JLabel("性别"));
        gender = new JTextField();
        north.add(gender);

        north.add(new JLabel("电话"));
        phone = new JTextField();
        north.add(phone);

        north.add(new JLabel("分数"));
        score = new JTextField();
        north.add(score);


        return north;
    }

    private JPanel southPanel(){//添加确定、取消按钮，实现功能
        JPanel south = new JPanel();
        GridLayout grid = new GridLayout(1,2);
        south.setLayout(grid);

        JButton ok = new JButton("确定");
        south.add(ok);
        ok.addActionListener(new OkAction());

        JButton cancel = new JButton("取消");
        south.add(cancel);
        cancel.addActionListener(new CancelAction());


        return south;
    }

    class OkAction implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            String n = name.getText();
            String a = age.getText();
            String g = gender.getText();
            String p = phone.getText();
            String s = score.getText();
            if(n ==null || n.equals("")){
                JOptionPane.showMessageDialog(null,"名字不能为空");
                return;
            }
            //UUID,全球通用唯一识别码 Universally Unique Identifier
            //8-4-4-4-12,16进制的字符串
            // xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
            String id = UUID.randomUUID().toString().replaceAll("-","").substring(0,9);
            //根据界面的输入构造学生对象
            Student stu = new Student(id,n,a,g,p,s);
            //把学生加入到数据库
            boolean isSuccess = SqliteDb.addStudent(stu);
            if (isSuccess){//添加成功
                JOptionPane.showMessageDialog(null,"添加成功");
                //刷新表格
                MainView.initTable(MainView.jTable, SqliteDb.queryStudent());
                //关闭添加学生的窗口
                dispose();
            }else {//添加失败
                JOptionPane.showMessageDialog(null,"添加失败");
            }
        }
    }
    class CancelAction implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            //关闭窗口
            dispose();
        }
    }



}

