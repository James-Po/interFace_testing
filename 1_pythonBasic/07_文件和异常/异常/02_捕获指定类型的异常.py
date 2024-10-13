try:
    num = input("请输入一个数字：")
    # 进行类型转换
    num = int(num)
    a = 10 / num
    print(a)
except ValueError:
    print("请输入正确的数字")

except ZeroDivisionError:
    print("除数不能为0")
