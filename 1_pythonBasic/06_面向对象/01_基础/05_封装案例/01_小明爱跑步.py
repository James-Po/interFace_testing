"""
需求：
1、小明体重75.0公斤
2、小明每次跑步会减重0.5公斤
3、小明每次吃东西会增重1公斤
"""

"""
类名: ⼈类(Person)
属性: 体重(weight)  姓名(name)
⽅法: 跑步(run)  ---> 修改属性值
吃东⻄(eat)  ---->  修改属性值
__init__  定义属性
__str__  打印属性信息使⽤
"""
class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'小明跑步,体重减0.5kg,当前体重为{self.weight}')

    def eat(self):
        self.weight += 1
        print(f'小明吃东西,体重增1kg,当前体重为{self.weight}')

    def __str__(self):
        return f'{self.name}的体重是{self.weight}'


if __name__ == '__main__':
    # 创建对象
    xming = Person('⼩明', 75.0)
    print(xming)
    xming.run()
    xming.eat()
    xmei = Person('⼩美', 45.0)
    print(xmei)
    xmei.run()
    xmei.run()
    xmei.eat()
