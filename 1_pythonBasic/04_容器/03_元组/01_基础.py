"""
1, 元组 tuple, 使用的 ()
2, 元组和列表非常相似, 都可以存储多个数据, 都可以存储任意类型的数据
3, 区别就是 元组中的数据不能修改,列表中可以修改
4, 因为元组中的数据不能修改,所以只能 查询方法, 如 index, count ,支持下标和切片
5, 元组, 主要用于传参和返回值
"""
# 1. 类实例化方式
# 1.1 定义空元组(不用)
tuple1 = tuple()
print(type(tuple1), tuple1)  # <class 'tuple'> ()
# 1.2 类型转换 , 将列表(其他可迭代类型)转换为元组
tuple2 = tuple([1, 2, 3])
print(tuple2)
# 2. 直接使用 () 定义
# 2.1 定义空元组
tuple3 = ()
# 2.2 非空元组
tuple4 = (1, 2, 'hello', 3.14, True)
print(tuple4)
print(tuple4[2])  # hello
# 2.3 定义只有一个数据的元组,  数据后必须有一个逗号
tuple5 = (10,)
print(tuple5)
