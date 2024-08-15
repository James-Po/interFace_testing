"""
局部变量
1, 在函数内部定义的变量,称为是局部变量
2, 特点-   2.1 局部变量,只能在当前函数内部使用-   2.2 可以在不同函数内定义名字相同的局部变量
3, 生命周期(使用范围)-   3.1 在函数执行(调用)的时候被创建-   3.2 函数执行结束被销毁(删除)
4, 形参可以认为是局部变量
5, 如果想要在函数外部使用局部变量的值, 使用 return 返回
"""


# def func1():
#     num = 10    # 局部变量
#     print(num)
#
#
# def func2():
#     num = 20
#     print(num)
#
#
# if __name__ == '__main__':
#     func1()  # 10
#     func2()  # 20
#     func1()  # 10

"""
全局变量
1, 在函数外部定义的变量
2, 特点-   
    2.1 全局变量 可以在任意函数内访问(读取)-   
    2.2 想要在函数内部修改全局变量的引用,需要使用 global 关键字声明(使用 global 关键字可以声明为全局变量)-   
    2.3 如果在函数内部出现和全局变量名字相同的局部变量,在函数内部使用的是局部变量
3, 生命周期-   代码执行的时候 创建, 执行结束销毁
"""
# g_num = 10
#
#
# def func_1():
#     print(g_num)    # use global variable
#
#
# def func_2():
#     g_num = 20      # 定义为局部变量
#     print(g_num)
#
#
# def func_3():
#     global g_num  # 声明为全局变量
#     g_num = 30
#     print(g_num)
#
#
# if __name__ == '__main__':
#     func_1()  # 10
#     func_2()  # 20
#     func_1()  # 10
#     print(g_num)  # 10
#     func_3()  # 30  修改了全局变量, 将全局变量的值改为30 了
#     func_1()  # 30
#     g_num = 100
#     func_1()  # 100  修改全局变量的值
#     func_2()  # 20  局部变量
#     func_3()  # 30
#     func_1()  # 30


def func1():
    list1.append(10)


def func2():
    list1 = [1, 1]      # 定义局部变量，不影响全局变量
    list1.append(0)


def func3():
    global list1
    list1.pop()


def func5():
    list1.pop()


def func4():
    global list1
    list1 = [1]


if __name__ == '__main__':
    list1 = [1, 2]
    func1()
    print(list1)  # ①[1, 2]  ②[1, 2, 10](√)  ③报错
    func2()
    print(list1)  # ① [1, 1, 0] ②[1, 2, 10](√) ③报错
    func3()
    print(list1)  # [1, 2]
    # func_5()
    # print(list1)  # ②[1, 2]   ①[1]对
    func4()
    print(list1)  # [1]