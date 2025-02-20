# 1、导包
import unittest

# 2、定义测试类，只要继承unittest.TestCase 类，就是 测试类
class TestDemo1(unittest.TestCase):
    # 3、书写测试方法，方法中的代码就是真正用例代码，方法名称必须以 test 开头
    def test_method1(self):
        print('这是个测试方法1-1')

    def test_method2(self):
        print('这是个测试方法1-2')


'''
4、执行
4.1 再类名或者方法名后边右键运行
4.1.1 在类名后面，执行类中的所有的测试方法
4.1.2 在方法名后边，只执行当前的测试方法
'''

# 4.1 在住程序使用 unittest.main() 来执行
# if __name__ == '__main__':
#     unittest.main()