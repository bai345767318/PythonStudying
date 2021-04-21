'''菜单栏'''

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,qApp,QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个菜单条目
        exitAction = QAction(QIcon('day07\exit3.png'),'退出',self)
        # 添加快捷键
        exitAction.setShortcut('Ctrl+Q')
        # 给菜单绑定动作
        exitAction.triggered.connect(qApp.quit)

        # 创建一个菜单栏
        menuBar = self.menuBar()
        # 添加菜单
        fileMenu = menuBar.addMenu('文件')
        # 添加菜单条目
        fileMenu.addAction(exitAction)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('菜单')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())