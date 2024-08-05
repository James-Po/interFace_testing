"""
字符串.find(sub_str)   # 在字符串中 查找是否存在 sub_str 这样的字符串
返回值(这行代码执行的结果):
1, 如果存在sub_str, 返回 第一次出现 sub_str 位置的下标
2, 如果不存在sub_str, 返回 -1
"""

# 1. 现有字符串数据: '黑马程序员'
# 2. 请设计程序, 实现判断"黑马"和"白马"是否存在于数据中
# 3. 要求如果数据存在, 则输出数据所在位置
# my_str = '黑马程序员'
# sub_str = input('please enter a string: ')
# result = my_str.find(sub_str)
# if result == -1:
#     print(f'{sub_str} is not found')
# else:
#     print(f'{sub_str} is found')


"""
字符串.replace(old, new, count)  # 将字符串中的 old 字符串 替换为 new 字符串
- old 原字符串,被替换的字符串- new 新字符串,要替换为的字符串
- count 一般不写,表示全部替换, 可以指定替换的次数
- 返回: 会返回一个替换后的完整的字符串
- 注意: 原字符串不会改变的
"""
# my_str = 'good good study'
# # 需求, 将 good 变为 GOOD
# my_str1 = my_str.replace('good', 'GOOD')
# print('my_str :', my_str)
# print('my_str1:', my_str1)
# # 将第一个 good 替换为 Good
# my_str2 = my_str.replace('good', 'Good', 1)
# print('my_str2:', my_str2)
# # 将第二个 good 替换为 Good
# # 先整体替换为 Good, 再将替换后的 第一个Good 替换为 good
# my_str3 = my_str.replace('good', 'Good').replace('Good', 'good', 1)
# print('my_str3:', my_str3)

"""
字符串.split(sep) # 将字符串按照指定的字符串 sep 进行分隔
- sep , 按照 sep 分隔, 可以不写, 默认按照空白字符(空格 \t \n)分隔
返回: 列表,列表中的每个数据就是分隔后的字符串
"""
# str1 = 'hello Python\tand itcast and\nitheima'
# # 1. 默认 按照空白字符分隔
# list1 = str1.split()
# print(list1)  # ['hello', 'Python', 'and', 'itcast', 'and', 'itheima']
# # 2. 按照 空格分隔
# list2 = str1.split(' ')
# print(list2)  # ['hello', 'Python\tand', 'itcast', 'and\nitheima']
# # 3. 按照 and 分隔
# list3 = str1.split('and')
# print(list3)  # ['hello Python\t', ' itcast ', '\nitheima']


"""
字符串.join(容器) # 容器一般是列表 , 将字符串插入到列表相邻的两个数据之间,组成新的字符串
注意点: 列表中的数据 必须都是字符串才可以
"""
list1 = ['hello', 'Python', 'and', 'itcast', 'and', 'itheima']
# 将列表中数据使用 空格 组成新的字符串
str1 = ' '.join(list1)
print(str1)  # hello Python and itcast and itheima
# 使用 逗号 连接
str2 = ','.join(list1)
print(str2)  # hello,Python,and,itcast,and,itheima
# 使用 _*_ 连接
str3 = '_*_'.join(list1)
print(str3)  # hello_*_Python_*_and_*_itcast_*_and_*_itheima
