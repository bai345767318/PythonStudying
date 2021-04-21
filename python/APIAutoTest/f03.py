'''
监控服务器的CPU、内存、磁盘、网络
'''


import psutil

print(psutil.cpu_percent())#cpu
print(psutil.virtual_memory())#内存
print(psutil.virtual_memory().percent)#内存百分比
print(psutil.disk_usage("d:/"))#磁盘
print(psutil.disk_usage("d:/").percent)#磁盘的百分比
print(psutil.net_io_counters())#网络IO
print(psutil.net_io_counters().bytes_sent)#发送的字节数
print(psutil.net_io_counters().bytes_recv)#接收的字节数


# 死循环，每隔3s获取数据，把数据写到文件中
# 首行：时间戳 CPU百分比 内存百分比 磁盘百分比 发送字节数 接收字节数

from datetime import datetime
from time import sleep
with open("d:/监控.txt",mode='a',encoding='utf-8') as f:
    f.write("时间\tCpu百分比\t内存百分比\t磁盘百分比\t发送字节数\t接收字节数\n")
    print("监控中")
    while True:
        print()
        t = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
        c = psutil.cpu_percent()
        v = psutil.virtual_memory().percent
        d = psutil.disk_usage("d:/").percent
        ns = psutil.net_io_counters().bytes_sent
        nr = psutil.net_io_counters().bytes_recv
        f.write(f"{t}\t{c}\t{v}\t{d}\t{ns}\t{nr}\n")
        f.flush()#从缓存写入文件
        sleep(3)






