import unittest
from urllib import response


class TestAdd:
    def test_login(self):
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()