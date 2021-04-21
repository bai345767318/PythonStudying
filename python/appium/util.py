from selenium import webdriver
from appium import webdriver as appwebdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import yaml,openpyxl,logging
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class BoxDriver:

    '''工具类'''
    def __init__(self,url=None,browser='Chrome',separator=' '):
        #打开百度文库
        desired_capabilities ={
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "appPackage": "com.baidu.wenku", #可删除
        "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity", #可删除
        "deviceName": "62001"
        }

        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Opera':
            self.driver = webdriver.Opera()
        elif browser == 'Safari':
            self.driver = webdriver.Safari()
        elif browser =='Ie':
            self.driver == webdriver.Ie()
        elif browser =='App':
            self.driver = appwebdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

        self.driver.implicitly_wait(10)
        
        if browser !='App':
            self.driver.maximize_window()
            self.driver.get(url)

        self.separator = separator

    def maximize_window(self):
        '''窗口最大化'''
        self.driver.maximize_window()

    def wait(self,second):
        '''
        休眠指定的时间
        second: 休眠的时间
        '''
        sleep(second)

    def implicitly_wait(self,second=10):
        '''
        隐式等待
        second: 最大等待时间
        '''
        self.driver.implicitly_wait(second)

    def web_driver_Wait(self,selector,timeout=5,poll_frequency=0.5):
        '''
        显示等待
        '''
        locator = self.convert_selector_to_locator(selector)
        return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(locator))

    def get(self,url):
        '''
        打开网页
        url : 网页的地址
        '''
        self.driver.get(url)

    def convert_selector_to_locator(self,selector):
        '''
        将自定义的selector转换为selenium标准定位格式
        'id kw' -> (By.ID,'kw')
        selector: 自定义元素定位方式
        '''
        args = selector.split(self.separator)
        by = args[0].strip()    #定位方式
        value = args[1].strip() #定位值
        if by == 'id' or by == 'i':
            locator = (By.ID,value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME,value)
        elif by == 'class' or by == 'c':
            locator = (By.CLASS_NAME,value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH,value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT,value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT,value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME,value)
        elif by == 'css_selector' or by == 'cs':
            locator = (By.CSS_SELECTOR,value)
        else:
            raise NameError('请输入一个合法的定位方式！')

        return locator

    def locate_element(self,selector):
        '''
        定位单个元素
        selector: 自定义元素定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        # return self.driver.find_element(locator[0],locator[1])
        return self.driver.find_element(*locator)

    def locate_elements(self,selector):
        '''
        定位多个个元素
        selector: 自定义元素定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        # return self.driver.find_element(locator[0],locator[1])
        return self.driver.find_elements(*locator)

    def click(self,selector):
        '''
        对元素进行单击操作
        selector: 自定义元素定位方式
        '''
        self.locate_element(selector).click()

    def input(self,selector,text):
        '''
        向元素发送信息
        selector: 自定义元素定位方式
        '''
        element = self.locate_element(selector)
        element.clear()
        element.send_keys(text)

    def switch_to_frame(self,selector):
        '''
        进入iframe
        '''
        frame = self.locate_element(selector)
        self.driver.switch_to.frame(frame)

    def select_by_index(self,selector,index):
        '''
        根据index选择下拉选择框的选项
        '''
        # 选中select元素
        select = self.locate_element(selector)
        # 使用Select进行处理
        options = Select(select)
        # 选择选项
        options.select_by_index(index) # 根据下标来选中

    def select_by_value(self,selector,value):
        '''
        根据value选择下拉选择框的选项
        '''
        # 选中select元素
        select = self.locate_element(selector)
        # 使用Select进行处理
        options = Select(select)
        # 选择选项
        options.select_by_value(value) 

    def select_by_visible_text(self,selector,visible_text):
        '''
        根据visible_text选择下拉选择框的选项
        '''
        # 选中select元素
        select = self.locate_element(selector)
        # 使用Select进行处理
        options = Select(select)
        # 选择选项
        options.select_by_visible_text(visible_text)

    def close(self):
        '''
        关闭当前窗口
        '''
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()
    
    def clear(self):
        self.driver.clear()

class BasePage:

    def __init__(self,driver:BoxDriver):
        self.driver = driver

class GetYaml:
    
    def get(self,path):
        with open(path,'r',encoding='utf-8') as file:
            return yaml.load(file.read(),Loader=yaml.SafeLoader)

class GetExcel:
    
    def get(self,path,worksheet):
        '''
        workbook    工作簿
        worksheet   工作表
        cell        单元格
        '''

        # 打开工作簿
        workbook = openpyxl.load_workbook(path)
        # 获取指定的工作表
        login_success = workbook[worksheet]
        # [('admin','123456','admin'),('tom','123456','Tom Cruse'),('user0','123456','user0')]
        return [tuple(cell.value for cell in row) for row in login_success][1:]
        # l = []
        # for row in login_success:
        #     t = []
        #     for cell in row:
        #         t.append(cell.value)
        #     print(t)
        #     l.append(tuple(t))
        # print(l)

class GetCSV:

    def get(self):
        with open(r'selenium\ranzhi\login_success.csv','r',encoding='utf-8') as file:
            text1 = file.read()
            # print(text1)
            text2 = text1.split('\n')
            # print(text2)
            l = [tuple(i.split(',')) for i in text2]
            # print(l)
        return l

class GetLogger:

    def __init__(self,path):
        # 日志文件路径
        self.path = path
        # 创建日志
        self.logger = logging.getLogger()
        # 指定日志输出的内容
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:[%(message)s]')
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

    def _output(self,level,message):
        # 创建一个fileHandler对象，将日志内容写入
        fh = logging.FileHandler(self.path,mode='a',encoding='utf-8')
        # 设置日志等级
        fh.setLevel(logging.DEBUG)
        # 设置日志的输出内容
        fh.setFormatter(self.formatter)
        # 将内容添加到日志文件
        self.logger.addHandler(fh)

        # 创建一个StreamHandler对象，输出到控制台
        sh = logging.StreamHandler(sys.stdout)
        # 设置日志等级
        sh.setLevel(logging.DEBUG)
        # 设置日志的输出内容
        sh.setFormatter(self.formatter)
        # 将内容添加到控制台
        self.logger.addHandler(sh)

        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        # 移除处理器
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        # 关闭文件
        fh.close()

    def debug(self,message):
        self._output('debug',message)

    def info(self,message):
        self._output('info',message)

    def warning(self,message):
        self._output('warning',message)

    def error(self,message):
        self._output('error',message)

    def critical(self,message):
        self._output('critical',message)

class SendMail:

    def send(self,receivers,path,server='smtp.163.com',port=25,sender='bjz17791434290@163.com',pwd='DHGXWFXPZRIXIUJQ'):
        '''
        server:邮件服务器地址
        port:邮件服务器端口
        sender:发件人地址-登陆账户
        pwd:邮箱密码
        recervers:收件人
        path:报告的路径
        '''
        # #右键服务器地址
        # server = 'smtp.163.com'
        # #邮件服务器端口号
        # port = 25

        # #发件人地址--登陆账户
        # sender = 'bjz17791434290@163.com'
        # #邮箱密码
        # pwd = 'DHGXWFXPZRIXIUJQ'
        # #收件人
        # receivers = 'bjz17791434290@163.com;maoalei666@163.com;houfujun07@163.com;'

        #创建邮件对象
        mail = MIMEMultipart()
        #填写发件人
        mail['from'] = sender
        #填写收件人
        mail['to'] = receivers
        #主题
        mail['subject'] = 'Ranzhi自动化测试报告'

        #读取报告内容
        # path = r'./report/report_2020-11-17 18-10-45.html'
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
        filename = path.split('/')[-1]
        attch['Content-Disposition'] = 'attchment;filename=%s'%filename
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



if __name__ == "__main__":
    GetLogger('ranzhi.log').info('测试一下代码')
    
    



