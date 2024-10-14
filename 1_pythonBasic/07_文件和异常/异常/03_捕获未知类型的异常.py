try:
    num = input("请输入一个数字：")
    # 进行类型转换
    num = int(num)
    a = 10 / num
    print(a)
except Exception as e:
    print("发生了异常", e)
