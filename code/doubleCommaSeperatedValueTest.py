import unittest

from code.doubleCommaSeperatedValue import doubleCommaValue


class MyTestCase(unittest.TestCase):
    def test_for_the_double_of_comma_seperated_value(self):
        value = "2,3,5"
        result = doubleCommaValue(value)
        self.assertEqual(result, [4, 9, 25])

    def test_for_another_test_case(self):
        value = "4,6,7,9"
        result = doubleCommaValue(value)
        self.assertEqual(result, [16, 36, 49, 81])


if __name__ == '__main__':
    unittest.main()
