"""
self 参数

1, 参函数的语法上来看, self 是形参, 名字可以任意的变量名, 只是我们习惯性叫 self
 2, 特殊点: self 是⼀个普通的参数, 按照函数的语法,在调⽤的时候,必须传递实参值, 原因, 是 Python 解释器⾃动的将
 调⽤这个⽅法的对象作为参数传递给 self

 所以 self 就是调⽤这个⽅法对象
"""


# class Cat:
#     def eat(self):
#         print(f'self:{id(self)} ')
#         print('猫吃鱼')
#
#
# tom = Cat()
# # 通过对象 调⽤类中的⽅法
# print(f'tom:{id(tom)}')
# tom.eat()   # tom  调⽤ ,self 就是 Tom
# tom.name = 'tom'
# print(tom.name)
#
#
# blue_cat = Cat()
# print(f'blue_cat:{id(blue_cat)}')
# blue_cat.eat()   # blue_cat 调⽤, self 就是 blue_cat
#
# print('-' * 50)



"""
属性
属性表示事物的特征.
可以给对象添加属性 或者获取对象的属性值.
给对象添加属性:
对象.属性名 = 属性值  # 添加或者修改
获取对象的属性值:
对象.属性名
在⽅法中操作属性(self 是对象):
 self.属性名 = 属性值
self.属性名
"""
class Cat:
    def eat(self):  # self 是调⽤这个⽅法的对象
        print(f'self:{id(self)}')
        print(f'⼩猫{self.name}爱吃⻥...')

# 创建对象
tom = Cat()
 # 通过对象 调⽤类中的⽅法
print(f"tom :{id(tom)}")
 # 给 Tom 对象添加 name 属性
tom.name = '汤姆'
print(tom.name)
tom.eat()
blue_cat = Cat()
print(f'blue:{id(blue_cat)}')
blue_cat.name = '蓝猫'
blue_cat.eat()