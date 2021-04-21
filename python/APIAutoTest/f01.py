'''
使用locust进行性能测试
'''
from locust import HttpUser, task, between


# 为要开展性能测试的功能创建一个类：从HttpUser继承
class CarRental(HttpUser):
    # 设置思考时间在1-5秒之间
    # wait_time 是HttpUser中定义的属性，名字不能写错
    # between 是HttpUser中定义的方法
    wait_time = between(1, 5)

    @task  # 用task修饰，表示声明了一个任务
    def loadAllMenu(self):
        # HttpUser中有一个client属性，使用这个属性发送get/post方法
        # 用法跟requests中get/post也一样
        ret = self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")
        assert ret.status_code == 200
    @task
    def loadAllCar(self):
        ret = self.client.get("/carRental/car/loadAllCar.action?page=1&limit=10")
        assert ret.status_code == 200
    @task
    def loadAllNews(self):
        ret = self.client.get("/carRental/news/loadAllNews.action?page=1&limit=10")
        assert ret.status_code == 200

# 在命令行中执行：locust -f f01.py  改端口号--web-host=127.0.0.1 --web-port=8088
# locust会启动一个web客户端，8089
# localhost:8089
