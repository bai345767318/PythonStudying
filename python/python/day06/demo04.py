'''框布局'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okBtn = QPushButton('确定')
        cancelBtn = QPushButton('取消')

        # 创建水平布局
        hbox = QHBoxLayout()
        hbox.addStretch(1) # 推动按钮向右
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        # 创建一个垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1) # 推动按钮向下
        vbox.addLayout(hbox)

        # 添加到当前窗口中
        self.setLayout(vbox)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('框布局')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())