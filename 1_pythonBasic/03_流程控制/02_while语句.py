import random
"""
1. 循环的初始条件(计数器)
2. 循环的终⽌条件
while 判断条件:
判断条件成⽴执⾏的代码
判断条件成⽴执⾏的代码
判断条件成⽴执⾏的代码
# 3. 计数器加1
# 1, 处于 while 缩进中的代码,称为是 while 的循环体
# 2, 执⾏顺序 1 2 3 2 3 2 3 2 3 2(条件不成⽴, 结束)
"""
# i = 0
# while i < 5:
#     print(f'这是第{i + 1}次循环')
#     i += 1
#
# i = 1
# num = 0
# while i <= 100:
#     num += i
#     i += 1
# print(num)
"""
死循环和⽆限循环  在程序执⾏层⾯上看起来是⼀样的, 都是代码⼀直执⾏不能停⽌.
死循环: 是由于 写代码的⼈ 不⼩⼼造成.  bug
⽆限循环: 是写代码的⼈ 故意这么写.
⽆限循环中,⼀般会存在⼀个 if 判断语句, 当这个判断语句的条件成⽴, 执⾏ break 语句,来终⽌循环.
关键字 break: 当程序代码执⾏遇到 break, break 所在的循环就会被终⽌执⾏.(终⽌循环)
关键字 continue: 当程序代码执⾏遇到 continue, continue 后续的代码不执⾏,但是会继续下⼀次的循环(结束本次循环,继续下⼀次循环)
 break 和 continue 只能⽤在循环中.
"""
# while True:
#     player = int(input('请出拳：石头1/剪刀2/布3'))
#     computer = random.randint(1,3)
#     if player == 0:
#         break
#     if player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
#         print('玩家胜利')
#     elif player == computer:
#         print('平局')
#     else:
#         print('电脑胜利')

