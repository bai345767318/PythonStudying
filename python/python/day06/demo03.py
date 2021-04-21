import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('用户:',self)
        lbl1.move(0,0)

        lbl2 = QLabel('密码:',self)
        lbl2.move(50,30)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('绝对定位')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())