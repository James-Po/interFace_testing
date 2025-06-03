from tools import add


class TestAdd:
    def test_add_1(self):
        print(0, 10, 10)
        if 10 == add(0, 10):
            print("测试通过")
        else:
            print("测试失败")

    def test_add_2(self):
        print(1, 5, 6)
        if 10 == add(1, 5):
            print("测试通过")
        else:
            print("测试失败")

    def test_add_3(self):
        print(9, 7, 16)
        if 10 == add(9, 7):
            print("测试通过")
        else:
            print("测试失败")