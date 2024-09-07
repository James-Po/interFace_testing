"""
1, 什么是重写?
重写是在子类中定义了和父类中名字一样的方法.
2, 重写的原因? 为什么重写?
父类中的代码不能满足子类对象的需要
3, 重写的方式
3.1 覆盖式重写
3.2 扩展式重写
"""
# 覆盖式重写

# class Dog:
#     def brak(self):
#         print('汪汪叫')
#
# class Xtq(Dog):
#     def brak(self):
#         print('嗷嗷叫')
#     pass
#
# Dog().brak()
# Xtq().brak()


# 扩展式重写

'''
父类中的功能还需要,只是添加了新的功能
方法:
1. 先在子类中定义和父类中名字相同的方法
2. 在子类的代码中 使用 super().方法名() 调用父类中的功能
3. 书写新的功能
'''
class Dog:
    def bark(self):
        print('汪汪叫')
        print('汪汪叫')

class Xtq(Dog):
    def bark(self):
        super().bark()
        print('嗷嗷叫')
        print('嗷嗷叫')


if __name__ == '__main__':
    Dog().bark()
    Xtq().bark()