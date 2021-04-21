'''工具栏'''

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon(r'day07\exit3.png'),'退出',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        # 创建一个工具栏
        toolBar = self.addToolBar('Exit')
        toolBar.addAction(exitAction)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('工具栏')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())