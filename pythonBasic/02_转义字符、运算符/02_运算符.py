"""
优先级: () > ** > * / // % > + -
% 的使⽤场景: 判断⼀个数字是不是偶数, 能被 2 整除的数是
偶数
数字 除以 2 余数是 0
"""
# 除法
print(9 / 2)

# 求商
print(9 // 2)

# 取余
print(9 % 20)
print(9 ** 2)
print('---------------------------------------------------------')

"""
> < >= <= 只能是相同类型之间进⾏⽐较 (数字和字符串之间不能使⽤)
"""
a = 5
b = 3
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

"""
逻辑运算符
and or not 是关键字
- and 逻辑与 并且, 连接两个条件, 只有都为 True, 结果才
为 True, ⼀假为假
- or 逻辑或 或者, 连接两个条件, 只要⼀个条件 为 True,
结果就为 True, ⼀真为真
- not 逻辑⾮ 取反, 本来是 True, 加上 not 变为False
"""
print(a > 5 and  b < 4)
print(a > 5 or b < 4)
print(a >= 5 or b >= 4)
print(a <= 5 or b <= 4)
print(a >= 5 or b >= 4)
print(a <= 5 or b <= 4)
print(not a >= b)
