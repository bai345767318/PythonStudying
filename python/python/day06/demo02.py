import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('消息提示框')
        self.show()

    # closeEvent()关闭事件
    # 当点击关闭按钮时，自动调用该方法
    def closeEvent(self,event):
        # 创建提示框

        reply = QMessageBox.question(self,'警告！','您确定要退出程序吗？',QMessageBox.Yes | QMessageBox.No,QMessageBox.No) #No高亮显示
        # 判断用户的选择
        if reply == QMessageBox.Yes:
            event.accept() # 接受事件
        else:
            event.ignore() # 忽略事件


if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())