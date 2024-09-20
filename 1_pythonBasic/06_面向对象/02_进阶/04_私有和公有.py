# 定义人类、姓名、年龄
class Person:
    def __init__(self, name, age):
        self.name = name

        if (age >= 0) and (age <= 150):
            self.__age = age
        else:
            self.__age = 0
            print("年龄不合法，已重置为0")
    def __str__(self):
        return f"name: {self.name}, age: {self.__age}"

    # 因为 年龄属性变为私有,不能在类外部修改,只能在类内部操作, 所以定义一个公有的方法, 去修改年龄
    def setAge(self, age):
        if (age >= 0) and (age <= 150):
            self.__age = age
        else:
            print("年龄不合法")


xw = Person("小王", 18)
print(xw)

xw.__age = 1000     # 不能修改私有属性 age 了
print(xw)

xw.setAge(10000)
print(xw)

xl = Person("小李", 1000000)
print(xl)