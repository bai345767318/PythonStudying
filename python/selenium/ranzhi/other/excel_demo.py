'''
workbook    工作簿
worksheet   工作表
cell        单元格
'''

import openpyxl

# 打开工作簿
workbook = openpyxl.load_workbook(r'ranzhi\data.xlsx')
# 获取指定的工作表
login_success = workbook['login_success']

# [('admin','123456','admin'),('tom','123456','Tom Cruse'),('user0','123456','user0')]
# l = []
# for row in login_success:
#     t = []
#     for cell in row:
#         t.append(cell.value)
#     print(t)
#     l.append(tuple(t))
# print(l)

l = [tuple(cell.value for cell in row) for row in login_success]
print(l)
        