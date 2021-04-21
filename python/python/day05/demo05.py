import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        # 调用父类的构造方法
        super().__init__()
        self.initUI()######???????

    def initUI(self):
        # 设置窗口位置和大小
        self.setGeometry(300,300,300,200)
        # 标题
        self.setWindowTitle('Icon')
        # 设置窗口图标
        self.setWindowIcon(QIcon(r'day05\f9.png'))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
