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
# for i in range(11):
#     print('遍历指定次数：', str1[i], i)

#  1-100 之间的类加和
# num = 0
# for i in range(101):
#     num += i
# print('求和的结果为：',num)

# 案例
# 1. 提示⽤户输⼊登录系统的⽤户名和密码
# 2. 校验⽤户名和密码是否正确(正确的⽤户名:admin、密
# 码:123456)
#  3. 如果⽤户名和密码都正确，打印“登录成功!”，并结束程序
# 4. 如果⽤户名或密码错误，打印“⽤户名或密码错误!”，提示⽤
# 户继续输⼊⽤户名和密码登录 5. 如果⽤户输⼊的⽤户名为
# “exit”，则退出程序
while True:
    username = input('Please input your name:')
    if username == 'exit':
        break
    pwd = input('Please input your password:')
    if username == 'admin' and pwd == '123456':
        print('login successful')
        break
    else:
        print('login failed,Please try again')