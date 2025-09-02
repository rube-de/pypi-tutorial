import unittest
from src.example_package_rube.example import add_one


class TestExample(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)


if __name__ == '__main__':
    unittest.main()