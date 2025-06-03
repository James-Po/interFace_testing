def set_password():
    password = input("请输入密码(长度最少八位):")
    if len(password) >= 8:
        return password
    else:
        raise Exception("密码长度不够")


def add(a, b):
    return a + b