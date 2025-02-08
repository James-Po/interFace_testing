import unittest

class TestDemo(unittest.TestCase):
    def test_method1(self):
        self.assertEqual(1, 1)
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()