"""
继承
1, 继承描述的是类与类之间的关系 is ... a
2, 继承的好处: 减少代码冗余,重复代码不需要多次书写, 提高编程效率

语法：
# class 类A(object):
# class 类A():
class 类A: # 默认继承 object 类, object 类 Python 中最原始的类
    pass
class 类B(类A): # 就是继承, 类 B 继承 类 A
    pass
# 类 A: 父类 或 基类
# 类 B: 子类 或 派生类
子类继承父类之后, 子类对象可以直接使用父类中的属性和方法

"""

# 1. 定义动物类，动物有姓名和年龄属性，具有吃和睡的行为
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name} 正在吃')
    def sleep(self):
        print(f'{self.name} 正在睡')

# 2. 定义猫类，猫类具有动物类的所有属性和方法，并且具有抓老鼠的特殊行为
class Cat(Animal):
    def catch_mouse(self):
        print(f'{self.name} 正在抓老鼠。。。。')

class Dog(Animal):
    def look_home(self):
        print(f'{self.name} 正在看家。。。。')

class XTQ(Dog):
    def fly(self):
        print(f'{self.name} 正在飞。。。。')

if __name__ == '__main__':
    ani = Animal('佩奇', 2)
    ani.eat()
    ani.sleep()
    cat = Cat('黑猫警长', 10)
    cat.eat()  # 调用 父类 animal 中的方法
    cat.sleep()  # 调用 父类 animal 中的方法
    cat.catch_mouse()  # 调用自己类的方法
    dog = Dog('旺财', 3)
    dog.eat()
    dog.sleep()
    dog.look_home()
    xtq = XTQ('哮天犬', 100)
    xtq.eat()
    xtq.sleep()
    xtq.look_home()
    xtq.fly()
