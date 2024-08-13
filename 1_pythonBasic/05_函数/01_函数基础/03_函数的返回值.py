"""
返回值: 函数执⾏的结果
print()  ---> None
input()  ---> 键盘输⼊的内容, 类型 字符串
type()   ---> 变量的数据类型
len()    ---> 容器⻓度
1, 在⼀个函数中,想要返回⼀个数据(想要有返回值), 需要使⽤ return 关键字
2, 为什么返回值?  在函数中可能通过各种代码,得到的数据结果,想要在函数外部使⽤,就需要使⽤返回值
3, 如果函数有返回值, ⼀般在调⽤的时候 会使⽤变量来接收(保存) 返回值, 以便后续使⽤
4, return 关键字的作⽤, - 将⼀个数据值返回到调⽤的地⽅- 函数遇到 return 会结束函数的执⾏
5, return 关键字只能⽤在函数中
6, 如果⼀个函数 没有写 return,可以认为 返回值是 None
"""


# 设计⼀个函数⽤于获取两个数中的较⼤数，数据来⾃于函数的参数
# def get_max(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# num = get_max(10, 21)
# print(num)


# demo
# 1. 定义名为 input_username 的函数, 获取⽤户输⼊的⽤户名
# 2. 定义名为 input_password 的函数, 获取⽤户输⼊的密码
# 3. 定义名为 login 的函数, 判断获取的⽤户名和密码信息
# 4. 要求当获取的⽤户名为:admin 并且密码为: 123456 时, 输
# 出“登录成功!”，否则提示“⽤户名或 密码错误!”
def input_username():
    return input('please input your username: ')


def input_pwd():
    return input('please input your password: ')


def login():
    if input_username() == 'admin' and input_pwd() == '123456':
        print('login success')
    else:
        print('login fail')


login()