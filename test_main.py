import unittest
from main import set_calc


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("1", set_calc('(1)'))

    def test_12(self):
        self.assertEqual("1-2", set_calc('(1,2)'))

    def test_blank(self):
        self.assertEqual("1-2", set_calc('(1 -2)'))
        self.assertEqual("1-3", set_calc('(1- 3 ) '))

    def test_range(self):
        self.assertEqual("1-2", set_calc('(1-2)'))
        self.assertEqual("1-3", set_calc('(1-3)'))

    def test_operator(self):
        self.assertEqual("1-2,4", set_calc('(1-2)or (4)'))
        self.assertEqual("1-2,5", set_calc('(1-2) or (5)'))
        self.assertEqual("1-2,5-7", set_calc('(1-2) or (5-7)'))

    def test_operator_all(self):
        self.assertEqual("3-6", set_calc('(1-6) and (3-9)'))
        self.assertEqual("1-9", set_calc('(1-6) or (3-9)'))
        self.assertEqual("1-2,7-9", set_calc('(1-6) xor (3-9)'))
        self.assertEqual("1-2", set_calc('(1-6) sub (3-9)'))

    # def test_huge_set(self):
    #    self.assertEqual("1-2147483647", set_calc('(1-2147483647)'))
    #    self.assertEqual("1-4294967295", set_calc('(1-4294967295)'))


if __name__ == '__main__':
    unittest.main()
