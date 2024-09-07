"""
多态: 调用代码的技巧
多态:不同的子类对象调用相同的方法，产生不同的执行结果
"""

class Dog:
    def game(self):
        print('狗在跑着玩')

class Xtq(Dog):
    def game(self):
        print('哮天犬在天上飞')

class Person:
    def play_withDog(self, dog):
        print('人和狗在玩', end='')
        dog.game()


if __name__ == '__main__':
    dog1 = Dog()
    xtq1 = Xtq()
    person = Person()

    person.play_withDog(xtq1)
    person.play_withDog(dog1)