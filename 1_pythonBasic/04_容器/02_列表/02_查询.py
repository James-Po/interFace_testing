"""
index()方法
index() 这个方法的作用和 字符串中的 find() 的作用是一样
列表中是没有 find() 方法的, 只有 index() 方法
字符串中 同时存在 find() 和 index() 方法

index()
1, 找到 返回下标
2, 没有找到, 直接报错
"""
"""
count()方法
列表.count(数据)  # 统计 指定数据在列表中出现的次数
"""
list1 = ['hello', 2, 3, 2, 3, 4]

# 查找 2 出现的下标
num = list1.index(2)
print(num)

# 统计数据 2 出现的次数
num1 = list1.count(2)
print(num1)

# 统计数据 20 出现的次数
num2 = list1.count(20)
print(num2)     # 0
