# 1、导包，unittest
import unittest
from yjp_basicCase import TestDemo1
from yjp_secondCase import TestDemo2

# 2、创建实例化套件对象 unittest.TestSuite()
suite = unittest.TestSuite()

# 3、添加用例方法
# 3,2 添加整个测试类
# # 套件对象.addTest(unittest.makeSuite(测试类名))
# suite.addTest(unittest.makeSuite(TestDemo1))
# suite.addTest(unittest.makeSuite(TestDemo2))  老版本写法

# 创建用例装载器对象
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestDemo1))
suite.addTests(loader.loadTestsFromTestCase(TestDemo2))         # 新版本写法

# 4、实例化执行对象 unittest.TextTestRunner()
runner = unittest.TextTestRunner()
runner.run(suite)