"""
需求
进⼊某 Web 项⽬登录⻚⾯，输⼊⽤户名、密码、验证码之后登录系统
"""


class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.verify_code = code

    def login(self):
        print(f"用户名：{self.username}")
        print(f"密码：{self.password}")
        print(f"验证码：{self.verify_code}")


if __name__ == '__main__':
    login_page = LoginPage("admin", "123456", "1234")
    login_page.login()