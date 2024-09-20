class Tools:
    count = 0  # 类属性, 统计 对象的个数

    def __init__(self, name):
        self.name = name
        Tools.count += 1  # 创建对象之后, 个数加1

    # 定义类方法
    @classmethod
    def show_tool_count(cls):  # cls 就是类对象,就是类,调用和 self 不需要传参
        print(f"当前对象的个数为: {cls.count} 个")

    # 定义静态方法
    @staticmethod
    def show_info():
        print('这是一个工具类')


# 查看当前对象的个数 (调用类方法)
Tools.show_tool_count()
t1 = Tools('洛阳铲')
# 可以使用对象 来调用类方法
t1.show_tool_count()
# 调用静态方法
Tools.show_info()
t1.show_info()