"""
增加和修改
字典['键'] = 值
# 1, 键 存在, 修改
# 2, 键 不存在, 添加
"""
# 定义非空字典, 姓名, 年龄, 身高, 性别
my_dict = {'name': '小明', 'age': 18, 'height': 1.78, 'isMen': True}
print(my_dict)

# 将年龄改为 20
my_dict['age'] = 20
print(my_dict)

# 添加 体重 weight
my_dict['weight'] = 65
print(my_dict)
print('------------------------------------------------------------------')


"""
典的删除是根据字典的键 删除键值对
字典.pop('键')
"""
my_dict.pop('weight')
print(my_dict)
my_dict.pop('height')
print(my_dict)