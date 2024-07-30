"""
单独的 if 语句,就是 如果 条件成⽴,做什么事
if 判断条件:
 判断条件成⽴,执⾏的代码
 判断条件成⽴,执⾏的代码
这⾏代码和if 判断⽆关
1, if 语句后边需要⼀个 冒号
2, 冒号之后 需要回⻋缩进(在 pycharm 中会⾃动的添加)
3, 处在 if 语句的缩进中的代码 可以称为是 if 语句的代码块(多⾏代码)
4, if 语句的代码块中的代码,要么都执⾏,要么都不执⾏
5, 如果某⾏代码 和if 的判断⽆关,就不需要写在 if 的缩进中
"""
import random
# 需求1:
# 1. 定义⼀个整数变量记录输⼊的年龄
# 2. 判断是否满 18 岁 (>=)
# 3. 如果满 18 岁，允许进⽹吧嗨⽪

# 定义一个变量，记录输入的年龄
# age = int(input('告诉我你多大了：'))
# # 判断是否满18岁，满则放进网吧，不满则滚蛋
# if age >= 18:
#     print('哥满 18 岁了, 可以进⼊⽹吧 为所欲为...')
# else:
#     print('滚蛋！')

# 练习1:
# 1. 获取⽤户输⼊的⽤户名信息
# 2. 如果⽤户名信息是 admin, 就在控制台输出 "欢迎admin登录"
# 获取用户的用户名
# userName = input('请输入您的用户名：')
# if userName == 'admin':
#     print('欢迎admin登录')
# else:
#     print('给爷爬！')

"""
if 和逻辑运算符结合
逻辑运算符 and or not
"""
# 案例1
# 1. 获取⽤户输⼊的⽤户名和密码
# 2. 判断⽤户名是 admin 并且密码是 123456 时, 在控制台输出: 登录成功!
# 3. 否则在控制台输出: 登录信息错误!
# userName = input('请输入您的用户名：')
# userPwd = input('请输入您的密码：')
# if userName == 'admin' and userPwd == '123456':
#     print('登录成功！')
# else:
#     print('登录信息错误！')

# 案例2:
# 1. 定义两个整数变量python_score、c_score，使⽤ input
# 获取成绩 编写代码判断成绩
# 2. 要求只要有⼀⻔成绩 > 60 分就输出合格
# python_score = int(input('输入你的Python语言课程成绩：'))
# c_score = int(input('输入你的C语言课程成绩：'))
# if python_score > 60 or c_score > 60:
#     print('成绩及格！')
# else:
#     print('小笨蛋！')

# 案例3:
# 1. 获取⽤户输⼊的⽤户名
# 2. 判断⽤户名是 admin 时, 在控制台输出: 欢迎 admin 登录!
# 3. ⽤户名是 test 时, 在控制台输出: 欢迎 test 登录!
# 4. 如果是其他信息, 在控制台输出: 查⽆此⼈!
# name = input('请输入您的用户名：')
# if name == 'admin' or name == 'test':
#     print(f'欢迎{name}登录！')
# else:
#     print('查无此人!')

"""
# if elif else 如果 ... 如果 ... 否则 ....
# 多个如果之间存在关系
if 判断条件1:
判断条件1成⽴,执⾏的代码
elif 判断条件2: # 判断条件1 不成⽴
 判断条件2成⽴,执⾏的代码
elif ....:
 pass
else:
 以上 判断条件都不成⽴,才会执⾏的代码
 
# 1, elif 是关键字, 后边需要冒号, 回⻋ 和缩进
# 2, if elif else 的代码结构, 如果某⼀个条件成⽴,其
他的条件就都不再判断
"""
# 需求
# 1. 定义 score 变量记录考试分数
# 2. 如果分数是 ⼤于等于 90分 显示 优
# 3. 如果分数是 ⼤于等于 80分 并且 ⼩于 90分 显示 良
# 4. 如果分数是 ⼤于等于 70分 并且 ⼩于 80分 显示 中
# 5. 如果分数是 ⼤于等于 60分 并且 ⼩于 70分 显示 差
# 6. 其它分数显示 不及格
# score = int(input('请输入您的分数：'))
# if score >= 90:
#     print('优秀')
# elif score >= 80 and score < 90:
#     print('良好')
# elif score >= 70 and score < 80:
#     print('中等')
# elif score >= 60 and score < 70:
#     print('及格')
# else:
#     print('垃圾！')

"""
if 嵌套
在⼀个if(elif else) 语句中 嵌套另⼀个 if(elif else ) 语句
判断条件存在递进关系才会使⽤. 即 只有第⼀个条件成⽴,才会判断第⼆个条件
"""
# 需求
# 取款机取钱的过程, 假定 你的密码是: 123456,  账户余额为 1000
# 1. 提示⽤户输⼊密码
# 2. 判断密码是否正确
# 3. 密码正确后,提示输⼊取款的⾦额,
# 4. 判断取款的⾦额和余额的关系
# balance = 1000
# userPwd = '123456'
# pwd = input('请输入取款密码：')
# if pwd == userPwd:
#     print('密码输入正确！')
#     outMoney = int(input('请输入要取走的金额（元）：'))
#     if outMoney <= balance:
#         print(f'领取成功！本次取出金额为{outMoney},余额为：{balance - outMoney}元')
#     if outMoney > balance:
#         print('您没有这么多钱！')
# else:
#     print('您的取款密码输入有误！')

# 练习
# 假定某⽹站⽤户名固定为 'admin', 密码固定为'123456',
# 验证码 固定为 '8888'
#  1. 获取⽤户输⼊的⽤户名,密码和验证码
# 2. 先判断验证码是否正确,如果正确打印输出验证码正确,再
# 判断⽤户名和密码是否正确
# 3. 如果验证吗不正确,直接输出 验证码不正确,请重新输⼊
# name = input('Please enter your name: ')
# pwd = input('Please enter your password: ')
# code = input('Please enter your code: ')
# if code == '8888':
#     print('code is right!')
#     if name == 'admin' and pwd == '123456':
#         print('login successful！')
#     else:
#         print('login failed,username or password is wrong')
# else:
#     print('code is false！')
