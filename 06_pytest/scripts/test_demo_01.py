
import pytest

# 书写测试类
class TestDemo01:
    # 书写测试方法（将来用来书写用例的真正代码），方法名以test开头
    def test_method_1(self):
        print('这是测试方法1')

    def test_method_2(self):
        print('这是测试方法2')

if __name__ == '__main__':
    pytest.main(['-s', 'test_demo_01.py'])