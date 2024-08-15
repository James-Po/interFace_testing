"""
多值参数(可变参数/不定长参数)
1, 在函数定义的时候,不确定在调用的时候,实参有多少个,此时可以使用 多值参数
2, 在普通的参数前边加上一个 *, 这个参数就变为 多值参数
3, 这个参数可以接收任意多个位置传参的数据, 类型 元组
4, 这个形参一般写作 args(arguments), 即 *args
"""

print(1)
print(1, 2)
print(1, 2, 3)
print(1, 2, 3, 4)

"""
# 普通, 缺省, 多值
def 函数名(普通, *args, 缺省):
    pass
"""


# def func(*args):
#     print(args)
#
#
# func()
# func(1, 2, 3)
print('-' * 30)


# practice
# 定义一个函数,my_sum,作用,可以对任意多个数字进行求和计算
def my_sum(*args):
    num = 0
    for i in args:
        num += i
    return num


print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4))
# 需求对 元组中的所有数据使用 my_sum 进行求和
# 想要把列表(元组) 中的数据作为位置参数进行传递, 只需要在列表(元组)前边加上一个 * ,进行拆包即可
my_tuple = (1, 2, 3, 4, 5)
print(my_sum(*my_tuple))

print('-' * 30)

#
# """
# 匿名函数: 使用 lambda 关键字 定义的表达式,称为匿名函数
# 语法：
# lambda 参数,
#     参数: 一行代码  # 只能实现简单的功能,只能写一行代码
# # 匿名函数 一般不直接调用, 作为函数的参数使用的
# """
#
# # practice
# # 1, 定义匿名函数, 参数为两个整数数字, 求两个数字的乘积
# lambda a, b: a * b
# # 2, 定义匿名函数, 参数为一个字典, 返回字典中 键为 age 的值
# lambda x : x.get('age')