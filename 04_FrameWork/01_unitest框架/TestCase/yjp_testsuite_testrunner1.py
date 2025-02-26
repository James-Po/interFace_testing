# 1、导包，unittest
import unittest

from yjp_basicCase import TestDemo1
from yjp_secondCase import TestDemo2

# 2、创建实例化套件对象 unittest.TestSuite()
suite = unittest.TestSuite()

# 3、添加用例方法
# 3,1 套件对象addTest(测试类名('测试方法名'))
suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))

suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))

# 4、实例化执行对象 unittest.TextTestRunner()
runner = unittest.TextTestRunner()
runner.run(suite)