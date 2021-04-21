'''表格布局'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 按钮的名称
        names = ['Cls','Back','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        
        # 创建网格中位置的列表
        positions = [(i,j) for i in range(5) for j in range(4)]

        # 创建表格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 创建按钮并添加到grid中
        for name,position in zip(names,positions):
            # if name == '':
            #     continue
            # 创建按钮
            btn = QPushButton(name)
            # 将按钮添加到grid中
            if name == 'Close':
                grid.addWidget(btn,0,2,1,2)
            else:
                grid.addWidget(btn,*position)

        self.setWindowTitle('计算器')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
