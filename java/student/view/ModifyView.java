package student.view;

import student.model.Student;
import student.utils.SqliteDb;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.UUID;

public class ModifyView extends JFrame {
    public JTextField  id,name, age, gender, phone, score;

    public  ModifyView() {
        this.add(northPanel(), BorderLayout.NORTH);
        this.add(southPanel(), BorderLayout.SOUTH);

        setTitle("修改学生信息");
        setBounds(650, 300, 500, 300);
        setVisible(true);
    }

        private JPanel northPanel () {
            JPanel north = new JPanel();
            GridLayout grid = new GridLayout(6, 2);//id让其自动生成
            north.setLayout(grid);

            //新建一个标签，放到中间容器中--对应的文本框
            north.add(new JLabel("id"));
            id = new JTextField();
            north.add(id);

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
        private JPanel southPanel () {//添加确定、取消按钮，实现功能
            JPanel south = new JPanel();
            GridLayout grid = new GridLayout(1, 2);
            south.setLayout(grid);

            JButton ok = new JButton("确定");
            south.add(ok);
            ok.addActionListener(new OkAction());

            JButton cancel = new JButton("取消");
            south.add(cancel);
            cancel.addActionListener(new CancelAction());


            return south;
        }

        class OkAction implements ActionListener {

            @Override
            public void actionPerformed(ActionEvent e) {
                String i = id.getText();
                String n = name.getText();
                String a = age.getText();
                String g = gender.getText();
                String p = phone.getText();
                String s = score.getText();
                if (i == null || i.equals("")) {
                    JOptionPane.showMessageDialog(null, "id不能为空");
                    return;
                }
                boolean c = SqliteDb.modifyStudent(i,n,a,g,p,s);
                if (c) {//修改成功
                    JOptionPane.showMessageDialog(null, "修改成功");
                    //刷新表格
                    MainView.initTable(MainView.jTable, SqliteDb.queryStudent());
                    //关闭添加学生的窗口
                    dispose();
                } else {//修改失败
                    JOptionPane.showMessageDialog(null, "修改失败");
                }
            }
        }
        class CancelAction implements ActionListener {

            @Override
            public void actionPerformed(ActionEvent e) {
                //关闭窗口
                dispose();
            }
        }

}
