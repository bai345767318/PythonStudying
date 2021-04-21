'''
PyQt5 - GUI graphic user interface 图形用户界面
'''
import sys
from PyQt5.QtWidgets import QWidget,QApplication

app = QApplication(sys.argv)
# QWidget类是pyqt5所有用户界面的基类
w = QWidget()
# 设置窗口的标题
w.setWindowTitle('你好！')
# 设置窗口大小
w.resize(250,150) # 宽，高 pixel: px
# 设置窗口的初始位置
w.move(300,300)
# 显示窗口
w.show()
# 保证程序干净的退出
sys.exit(app.exec_())
