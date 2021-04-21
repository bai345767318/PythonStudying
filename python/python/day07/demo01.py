'''状态栏'''

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个状态栏
        bar = self.statusBar()
        # 向状态栏写入信息
        bar.showMessage('准备好了')

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('状态栏')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())