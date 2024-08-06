"""
列表的反转 reverse()
字符串 反转 字符串[::-1]

列表 反转
1. 列表[::-1]   得到一个新列表, 原列表不会改动
2. 列表.reverse()  直接修改原列表的数据
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 切片
my_list1 = my_list[::-1]
print('my_list', my_list)
print('my_list1', my_list1)

# reserve函数
my_list.reverse()
print('my_list', my_list)
print('--------------------------------')

"""
列表的排序

前提: 列表中的数据要一样
列表.sort()  # 升序, 从小到大, 直接在原列表中进行排序
列表.sort(reverse=True) # 降序, 从大到下, 直接在原列表中进行排序
"""
list1 = [8, 2, 6, 4, 5, 3, 7, 1, 9]

# asc
list1.sort()
print('list1', list1)

# desc
list1.sort(reverse=True)
print('list1', list1)
print('--------------------------------')


"""
列表的嵌套
列表的嵌套 就是指 列表中数据都是列表.
"""

stu_list = [["张三", "18", "功能测试"], ["李四", "20", "自动化测试"], ["王五", "21", "自动化测试"]]
# 张三
print(stu_list[0][0])
# 李四
print(stu_list[0][1])
# 添加性别
stu_list[0].append('男')
print(stu_list)
# 删除性别
stu_list[0].pop()
print(stu_list)
# 打印所有的年龄
for info in stu_list:
    print(info[1])