import unittest
from data_types import data_type

class Datatype(unittest.TestCase):
    def test_return_when_argument_is_none(self):
        self.assertEqual(data_type(None), 'no value',
                         msg='Should return no value for no arg')

    def test_return_when_argument_is_string(self):
        self.assertEqual(data_type('hi'), 2,
                         msg='Should return string length for strings')

    def test_return_when_argument_is_bool(self):
        self.assertEqual(data_type(True), True,
                         msg='Should return function arg for bool types')

    def test_argument_less_than_100 (self):
        self.assertEqual(data_type(5), 'less than 100',
                         msg='Should return les than 100')

    def test_argument_more_than_100 (self):
        self.assertEqual(data_type(115), 'more than 100',
                         msg='Should return more than 100')

    def test_argument_equal_to_100 (self):
        self.assertEqual(data_type(100), 'equal to 100',
                         msg='Should return equal to 100')

    def test_list_arg(self):
        self.assertEqual(data_type([1, 2, 3, 4, 5]), 3,
                         msg='Should return third value for list')

    def test_small_list_arg(self):
        self.assertEqual(data_type([1, 2]), None,
                         msg='Should return None for small lists')

    def test_funciton_arg(self):
        def hello(*arg):
            pass
        self.assertTrue(data_type(hello()),
                        msg='Should return True for function args')


if __name__ == '__main__':
    unittest.main()
