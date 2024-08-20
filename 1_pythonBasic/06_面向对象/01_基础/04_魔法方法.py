"""
在Python 中存在⼀类⽅法, 以两个下划线开头, 两个下划线结
尾, 在满⾜某个条件的情况下,会⾃动调⽤,  这⼀类⽅法 称为是
魔法⽅法
怎么学习:
 1, 什么情况下会⾃动调⽤(⾃动调⽤的时机)
 2, 应⽤场景
3, 注意事项
"""

"""
初始化⽅法 __init__

1, 调⽤时机
在创建对象之后,会⾃动调⽤. 
2, 应⽤场景
初始化对象, 给对象添加属性
3, 注意事项- 不要写错- 如果 属性是会变化的, 则可以将这个属性的值作为参数传递, 在创建对象的时候,必须传递实参值
"""

class Cat:
    def __init__(self, name):
        print("初始化对象，我是init方法，我被调用了")
        self.name = name
    def eat(self):
        print(f'{self.name}在吃东西')

# init ⽅法 创建对象之后 会⾃动调⽤
# 1 会  2 不会
# Cat  # 2 不是创建对象
# Cat()   # 1 因为是创建对象
# tom = Cat   # 2  不是创建对象, 即 tom  也是类
#
# blue = Cat()  # 1 创建对象
# b = blue  # 2 不是创建对象, 只是引⽤的传递
#
# t = tom()   # 1, tom  已经是类, 类名()  就是创建对象


blue_cat = Cat("蓝猫")
blue_cat.eat()

black_cat = Cat("黑猫")
black_cat.eat()


"""
__str__ ⽅法
1, 调⽤时机
使⽤ print(对象)  打印对象的时候, 会⾃动调⽤
1, 如果没有定义 __str__ ⽅法, 默认打印的是 对象的引⽤地址
2, 如果定义 __str__ ⽅法,打印的是 ⽅法的返回值
2, 应⽤场景
使⽤ print(对象)  打印输出对象的属性信息
3, 注意事项
必须返回⼀个 字符串
"""


"""
定义 Cat 类, 包含属性 name 和 age, 打印对象的时候,可以
输出对象的姓名和年龄
类名: Cat
属性: name, age
⽅法: __str__ ,  __init__
"""

class Cat1:
    # 定义一个初始化方法，用于创建类的实例
    # 参数:
    #   name: 实例的名称
    #   age: 实例的年龄
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写字符串表示方法，返回实例的详细信息
    # 返回: 包含实例名称和年龄的字符串
    def __str__(self):
        return f'{self.name}的年龄是{self.age}'


# 创建一个名为tom的猫科动物实例，年龄为12岁
tom = Cat1("tom", 12)

# 输出tom对象的信息
print(tom)
