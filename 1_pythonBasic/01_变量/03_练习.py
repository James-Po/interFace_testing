# 需求:
# 1. 提示⽤户输⼊两个数字
# 2. 使⽤获取到的数据进⾏加法运算
# 3. 在控制台输出计算结果，格式要求:xx + xx = xx

# 练习1
# input接收的字符默认为string
num1 = int(input('Please input first number:'))
num2 = int(input('Please input second number:'))

# 格式化输出相加
sum1 = num1 + num2

# 格式1
print(f'{num1} + {num2} = {sum1}')
# 格式2
print('{} + {} = {}'.format(num1, num2, sum1))
