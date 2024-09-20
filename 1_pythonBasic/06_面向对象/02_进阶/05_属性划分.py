"""
1. 定义一个 工具类
2. 每件工具都有自己的 name
3. 需求 —— 知道使用这个类，创建了多少个工具对象?
"""

class Tools:
    # 在类内部,方法外部,直接定义的变量,就是类属性
    count = 0

    def __init__(self, name):
        self.name = name  # 名字
        # 每创建一个对象.就会调用 init 方法, 所以在这个方法中,对类属性进行加1操作
        Tools.count += 1


# 创建对象
print(f'当前创建的工具对象个数为: {Tools.count}个')
t1 = Tools('扳手')  # 创建一个对象之后, 个数应该加1,
print(f'当前创建的工具对象个数为: {Tools.count}个')
t2 = Tools('锤子')
print(f'当前创建的工具对象个数为: {Tools.count}个')