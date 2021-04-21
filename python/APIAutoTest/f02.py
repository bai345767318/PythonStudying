'''
任务集合，以分层的方式，按模块管理
'''
import math

from locust import TaskSet, task, HttpUser, between, LoadTestShape


#基础模块
class Basic(TaskSet):
    #客户管理
    # min_wait = 1
    # max_wait = 5
    # wait_function = None
    @task
    def custom(self):
        ret = self.client.get("/carRental/bus/toCustomerManager.action")
        assert ret.status_code == 200
    #车辆管理
    @task
    def car(self):
        ret = self.client.get("/carRental/bus/toCarManager.action")

#业务管理
class Business(TaskSet):
    # min_wait = 1
    # max_wait = 5
    # wait_function = None
    #出租单管理
    @task
    def rent(self):
        ret = self.client.get("/carRental/bus/toRentManager.action")
        assert ret.status_code == 200

#系统管理
class System1(TaskSet):
    # min_wait = 1
    # max_wait = 5
    # wait_function = None
    #角色管理
    @task
    def role(self):
        ret = self.client.get("/carRental/sys/toRoleManager.action")
        assert ret.status_code == 200

    # 用户管理
    @task
    def a_user(self):
        ret = self.client.get("/carRental/sys/toUserManager.action")
        assert ret.status_code == 200

class CarRental(HttpUser):
    def on_start(self):#前置
        user = {"loginname":"admin","pwd":"123456"}
        ret = self.client.post("/carRental/login/login.action",data=user)

    def on_stop(self):#后置
        ret = self.client.post("/carRental")#停止时执行
        # ret = self.client.post("/carRental/login/logout.action")#乱写的，执行出错
        assert ret.status_code == 200

    #任务的列表(tasks是HttpUser中定义的属性，单词不能写错)
    # tasks = [System1,Basic,Business]
    #任务还可以是字典，字典中的value表示权重，也就是如果10份，Syetem1的接口发送1份，Basic:6份，Business:3份
    tasks = {System1:1,Basic:6,Business:3}
    #思考时间(wait_time是是HttpUser中定义的属性，单词不能写错)
    wait_time = between(3,8)

# 在命令行中执行：locust -f f02.py


class StepLoadShape(LoadTestShape):#添加加压测试模型
    step_time = 30#两个批次之间的时间
    step_load = 10#每个批次增加多少用户
    spawn_rate = 10#用户上线的速率
    time_limit = 600#测试持续的时长5min

    def tick(self):
        #获取当前性能测试执行了多长时间
        run_time = self.get_run_time()
        #如果大于time_limit设置的值，则退出
        if run_time > self.time_limit:
            return None
        #计算当前是第几个批次
        current_step = math.floor(run_time / self.step_time) + 1
        #返回当前批次的用户数，以及速率
        return (current_step * self.step_load, self.spawn_rate)

#执行方式  C:\Python38\Scripts\locust.exe -f -fo2.py --web-host=127.0.0.1  --web-port=8088