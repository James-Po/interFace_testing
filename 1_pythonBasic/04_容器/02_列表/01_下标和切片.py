"""
1, 列表,list, 使用 []
2, 列表可以存放任意多个数据
3, 列表中可以存放任意类型的数据
4, 列表中数据之间 使用 逗号隔开
"""
# 方式1, 使用类实例化的方式
# 1.1 定义空列表 变量 = list()
list1 = list()
print(type(list1), list1)  # <class 'list'> []

# 1.2 定义非空列表 , 也称为 类型转换 list(可迭代类型) 可迭代类型,能够使用 for 循环 就是 可迭代类型(比如 容器)
# 将容器中的 每个数据 都作为列表中一个数据进行保存
list2 = list('abcde')
print(type(list2), list2)  # <class 'list'> ['a', 'b', 'c', 'd', 'e']

# 方式2, 直接使用 [] 进行定义(使用较多)
# 2.1 定义空列表
list3 = []
print(type(list3), list3)   # <class 'list'> []

# 2.2 定义非空列表
list4 = [1, 3.14, 'hello', False]
print(type(list4), list4)   # <class 'list'> [1, 3.14, 'hello', False]


