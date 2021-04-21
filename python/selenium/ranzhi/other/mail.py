from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#右键服务器地址
server = 'smtp.163.com'
#邮件服务器端口号
port = 25

#发件人地址--登陆账户
sender = 'bjz17791434290@163.com'
#邮箱密码
pwd = 'DHGXWFXPZRIXIUJQ'
#收件人
receivers = 'bjz17791434290@163.com;maoalei666@163.com;houfujun07@163.com;'

#创建邮件对象
mail = MIMEMultipart()
#填写发件人
mail['from'] = sender
#填写收件人
mail['to'] = receivers
#主题
mail['subject'] = 'Ranzhi自动化测试报告'

#读取报告内容
path = r'./report/report_2020-11-17 18-10-45.html'
with open(path,'rb') as file:
    report = file.read()

#邮件正文
#创建HTML格式的消息对象
body = MIMEText(report,'html','utf-8')#转换
#将报告作为正文添加到邮件中
mail.attach(body)

#邮件附件
attch = MIMEText(report,'base64','utf-8')#转换
#指定附件的类型
attch['Content-Type'] = 'application/octet-stream'
#指定附件的处理方式
attch['Content-Disposition'] = 'attchment;filename=%s'%path.split('/')[-1]
#添加附件
mail.attach(attch)

'''发送邮件'''
#创建服务器对象
smtp = smtplib.SMTP()
#连接服务器
smtp.connect(server,port)
#登录
smtp.login(sender,pwd)
#发送
smtp.sendmail(sender,receivers.split(';'),mail.as_string())
#关闭服务器
smtp.close()
print('邮件发送完毕')
