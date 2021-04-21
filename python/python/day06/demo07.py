'''计算器'''
#运算还有点问题
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QLineEdit
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个显示器
        self.screen = QLineEdit()
        self.screen.setAlignment(Qt.AlignRight) # 右对齐
        self.screen.setReadOnly(True) # 设置为只读

        # 按钮的名称
        names = ['Cls','Back','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        
        # 创建网格中位置的列表
        positions = [(i,j) for i in range(1,6) for j in range(4)]
        
        # 创建表格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 将显示器添加到表格中
        grid.addWidget(self.screen,0,0,1,4)

        # 创建按钮并添加到grid中
        for name,position in zip(names,positions):
            # if name == '':
            #     continue
            # 创建按钮
            btn = QPushButton(name)
            # 给按钮绑定事件
            btn.clicked.connect(self.action)##########??????
            # 将按钮添加到grid中
            if name == 'Close':
                grid.addWidget(btn,1,2,1,2)
            else:
                grid.addWidget(btn,*position)#传参时，元组(1,2)等价于1,2   

        self.setWindowTitle('计算器')
        self.show()

    def action(self):
        # 获取当前按下的按钮的文本
        text = self.sender().text()###########sender()意思
        if text == 'Cls':
            self.clear()
        elif text == 'Back':
            self.backsapce()
        elif text == 'Close':
            self.close()
        elif text == '=':
            self.calculate()
        else:
            self.show_msg(text)


    def clear(self):
        self.screen.setText('')

    def backsapce(self):
        content = self.screen.text()##字符串
        self.screen.setText(content[:-1])

    def close(self):
        quit()

    def calculate(self):
        # 获取屏幕的内容
        content = self.screen.text()
        try:
            result = eval(content)
        except:
            result = 'error'
        finally:
            self.screen.setText(str(result))

    def show_msg(self,text):
        content = self.screen.text()
        if content == 'error':
            content = ''
            self.clear()
        self.screen.setText(content+text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
