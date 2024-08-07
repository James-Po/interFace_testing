"""
print() 在控制台输出
input() 获取控制台输⼊的内容
type()  获取变量的数据类型
len()   获取容器的⻓度 (元素的个数)
range() ⽣成⼀个序列[0, n)
函数可以实现⼀个特定的功能
我们学习⾃⼰如何定义函数, 实现特定的功能
函数: 将多⾏代码(可以实现⼀个特定的功能)放在⼀块,并给它起⼀个名字. 在需要使⽤多⾏代码的时候, 可以使⽤名字代替.
定义函数的好处: 减少代码冗余(重复的代码不需要多次书写),提⾼编程效率
"""
# 定义和调用
"""
# 定义
1, 函数定义,就是给多⾏代码起名字的过程
2, 函数的定义需要使⽤ 关键字  def, 单词 define

def 函数名():
函数中的代码
函数中的代码
# 1, 处在 def 缩进中的代码 都属于这个函数
# 2, 函数名要满⾜标识符的规则, ⻅名知意
# 3, def 这⾏代码的最后需要⼀个 冒号
# 4, 函数定义不会执⾏函数中的代码,想要执⾏,需要调⽤
"""
"""
# 调用
1, 函数调⽤,就是使⽤ 多⾏代码的过程
2, 语法  函数名()
定义函数的⼩技巧
1, 先不使⽤函数,将多⾏代码写完
2, 在多⾏代码的上⽅使⽤ def 起名字
3, 使⽤ tab 键, 将多⾏代码进⾏缩进
"""
"""
# 函数的⽂档注释[了解]
1, 函数的⽂档注释,本质就是注释, 只不过作⽤和书写位置有特定的要求
2, 作⽤: 是对函数的作⽤和使⽤⽅法进⾏说明, ⽐如 有哪些参数, 返回值是什么
3, 书写位置: 在def 的下⽅,使⽤ 三对双引号来书写
----
查看
4.1 在函数名上,使⽤快捷键 Ctrl q 查看
4.2 在函数名上,使⽤ 快捷键 Ctrl B  跳转到函数定义的地⽅
查看
4.3 在函数名上, 按住 Ctrl 键,点击函数名,跳转到函数定义的地⽅查看
"""
# 参数的定义
"""
参数: 在函数定义的时候,在括号中写⼊变量,这个变量就称为是函数的参数.  形式参数(形参)
在函数调⽤的时候,可以给定义时候的形参传递具体的数据值,供其使⽤.  实际参数(实参)
即: 在函数调⽤的时候,会将函数的实参值传递给形参.

好处: 可以让函数更加的通⽤, 函数中的数据值不是固定的,是调⽤的时候,你传递的.
使⽤场景: 判断 函数中 数据值是不是固定不变的, 如果是变化的,就可以使⽤参数传递
注意点: ⽬前书写的函数, 如果存在形参,必须传递相同个数的实参.
"""

# def sum_two_numbers(num1, num2):
#     return num1 + num2
#
#
# sum_two_numbers(1, 2)
# print(sum_two_numbers(1, 2))
#
# sum_two_numbers(2, 6)
# print(sum_two_numbers(2, 6))


# 函数的嵌套调用
"""
在⼀个函数中调⽤另⼀个函数.
1, 代码从上到下执⾏的
2, 函数定义不会执⾏函数中的代码
3, 函数调⽤会进⼊函数中执⾏函数中的代码
4, 函数中的代码执⾏结束,会回到调⽤的地⽅继续向下执⾏
"""


# 定义一个test01函数，在函数内打印打印函数名称
def test01():
    print(1)
    print('test01')
    print(2)


# 定义一个test01函数，在函数内打印打印函数名称,并调用test02函数
def test02():
    print(3)
    print('func2')
    test01()
    print(4)


print(5)
test02()
print(6)