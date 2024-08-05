"""
1, 使用切片操作, 可以一次性获取容器中的多个数据(多个数据之间存在一定的规律,数据的下标是 等差数列(相邻的两个数字之间的差值是一样的))
2, 语法 容器[start:end:step]
2.1 start 表示开始位置的下标
2.2 end 表示结束位置的下标,但是 end 所对应的下标位置的数据是不能取到的
2.3 step 步长,表示的意思就是相邻两个坐标的差值
start, start+step, start+step*2, ...,end(取不到)
"""
my_str = 'abcdefg'

# 需求1 : 打印字符串中 abc 字符 start 0, end 3, step 1
print(my_str[0:3:1])  # abc
# 1.1 如果步长是 1, 可以省略不写
print(my_str[0:3])  # abc
# 1.2 如果 start 开始位置的下标为 0, 可以不写,但是冒号不能少
print(my_str[:3])  # abc
# 需求 2: 打印字符串中的 efg , start 4, end 7, step 1
print(my_str[4: 7])  # efg
# 2.1 如果取到最后一个字符, end  可以不写,但是冒号不能少
print(my_str[4:])  # efg
# 需求 3: 打印字符串中的 aceg , start 0, end 7(最后), 步长 2
print(my_str[::2])  # aceg
# 练习: cf
print(my_str[2:6:3])
# 特殊情况, 步长为 -1, 反转(逆序) 字符串
print(my_str[::-1])
# gfedcba