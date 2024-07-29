"""
for 循环 也称为是 for 遍历, 也可以做指定次数的循环
遍历: 是从容器中将数据逐个取出的过程.
容器: 字符串/列表/元组/字典
"""
# No.1
# for循环遍历字符串
str1 = 'yangjiangpo123'

# 使用for循环遍历
# for i in str1:
#      print('循环遍历：', i)

# NO.2
# 指定次数的循环
for i in range(11):
    print('遍历指定次数：', str1[i], i)