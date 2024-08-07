"""
in操作符

in 是 Python 中的关键字.
数据 in 容器 可以⽤来判断 容器中是否包含这个数据, 如果
包含返回 True,如果不包含返回 False
对于字典来说,判断的是 字典中是否包含这个键
"""
"""
集合

集合 set, {数据, 数据, ...}
1, 集合中的数据是不能重复的, 即没有重复数据
2, 应⽤, 对列表进⾏去重操作 就是类型转换 , 可以将列表转换为集合, 然后再将集合转换为列表
"""
my_list = [1, 2, 1, 2, 5, 2, 2, 4, 13]

# 方式一
list1 = list(set(my_list))
print(list1)

# 方式二
# new_list = []
# for i in my_list:
#     if i in new_list:
#         pass
#     else:
#         new_list.append(i)

new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)