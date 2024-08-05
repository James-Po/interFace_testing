"""
字符串.find(sub_str)   # 在字符串中 查找是否存在 sub_str 这样的字符串
返回值(这行代码执行的结果):
1, 如果存在sub_str, 返回 第一次出现 sub_str 位置的下标
2, 如果不存在sub_str, 返回 -1
"""

# 1. 现有字符串数据: '黑马程序员'
# 2. 请设计程序, 实现判断"黑马"和"白马"是否存在于数据中
# 3. 要求如果数据存在, 则输出数据所在位置
my_str = '黑马程序员'
sub_str = input('please enter a string: ')
result = my_str.find(sub_str)
if result == -1:
    print(f'{sub_str} is not found')
else:
    print(f'{sub_str} is found')


"""
字符串.replace(old, new, count)  # 将字符串中的 old 字符串 替换为 new 字符串
- old 原字符串,被替换的字符串- new 新字符串,要替换为的字符串
- count 一般不写,表示全部替换, 可以指定替换的次数
- 返回: 会返回一个替换后的完整的字符串
- 注意: 原字符串不会改变的
"""