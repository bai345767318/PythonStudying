import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QToolTip
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置提示的字体
        QToolTip.setFont(QFont('SansSerif',10)) # 参数1： 字体；参数2：字体大小

        # 设置当鼠标悬停在窗口上时显示提示
        self.setToolTip('这是一个QWidget组件')

        # 创建一个button
        btn = QPushButton('按钮',self)

        # 鼠标悬停在按钮上时显示
        btn.setToolTip('这是一个按钮组件')

        # 设置按钮大小
        btn.resize(btn.sizeHint())

        # 设置按钮位置
        btn.move(100,100)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tip')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())