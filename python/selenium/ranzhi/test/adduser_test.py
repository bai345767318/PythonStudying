from util import BoxDriver
from login_page import LoginPage
from adduser_page import AddUser

class AddUserTest:

    def adduser_test(self):
        driver = BoxDriver()
        addUser = AddUser(driver)
        addUser.login()
        addUser.add_user()

if __name__ == "__main__":
    AddUserTest().adduser_test()