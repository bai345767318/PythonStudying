'''文本框'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QGridLayout,QLineEdit,QTextEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建标签
        title = QLabel('标题')
        author = QLabel('作者')
        review = QLabel('简介')

        # 创建文本框
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # 创建表格布局
        grid = QGridLayout()

        grid.addWidget(title,0,0)
        grid.addWidget(titleEdit,0,1)

        grid.addWidget(author,1,0)
        grid.addWidget(authorEdit,1,1)

        grid.addWidget(review,2,0)
        grid.addWidget(reviewEdit,2,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,250,300)
        self.setWindowTitle('文本框')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

