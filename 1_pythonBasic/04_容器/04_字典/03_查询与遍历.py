"""
查询
根据字典的 键, 获取对应的 值.

方法一:
字典['键']   # 键 不存在,会报错

# 方法 二
字典.get(键)   # 键不存在,返回 None
"""
my_dict = {'name': '小明', 'age': 20}

# 获取 name 值
print(my_dict['name'])
print(my_dict.get('name'))

# 获取 性别 sex
# print(my_dict['sex'])   # 会报错, 因为 键不存在
print(my_dict.get('sex'))

"""
遍历
"""
# 字典存在 键(key), 值(value) , 遍历分为三种情况
# 遍历字典的键
"""
# 方式一
for 变量 in 字典:
    print(变量)

# 方式二
for 变量 in 字典.keys():  # 字典.keys() 可以获取字典所有的键
    print(变量)
"""
# 遍历字典的值[使用较多]
"""
for 变量 in 字典.values():  # 字典.values() 可以获取字典中是所有的值
    print(变量)
"""
for value in my_dict.values():
    print(value)
print('-' * 30)
"""
遍历字典的键和值
变量1 就是 键,  变量2 就是值
for 变量1, 变量2 in 字典.items():  #  字典.items() 获取的是字典的键值对
    print(变量1, 变量2)
"""
my_dict = {'name': '小明', 'age': 18, 'sex': '男'}

for k in my_dict:
    print(k)

print('*' * 30)
for k in my_dict.keys():
    print(k)

print('-' * 30)
for v in my_dict.values():
    print(v)

print('_*_' * 30)
for k, v in my_dict.items():
    print(k, v)
