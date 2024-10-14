"""
try:
    可能发生异常的代码
except 异常类型:
    发生了指定异常类型,执行的代码
except Exception as 变量:
    发生了其他类型的异常执行的代码
else:
    没有发生异常,执行的代码
finally:
    不管有没有发生异常,都会执行的代码
"""

'''
1. 获取用户输入的数字(input)
2. 判断获取的数字是否整数 (方式 1. 直接使用 int() 类型转换,没有发生异常就是整数,      方式2, 字符串.isdigit() 用来判断字符串是否都是纯数字)
3. 如果不是整数, 提示输入错误
4. 如果是整数, 则进一步判断是奇数还是偶数
5. 最终提示: 程序运行结束
'''
try:
    num = int(input("请输入一个数字:"))
except Exception as e:
    print("输入有误！", e)

else:
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
finally:
    print("程序运行结束")