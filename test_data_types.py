import unittest
from data_types import data_type

class Datatype(unittest.TestCase):
    def test_return_when_argument_is_none(self):
        self.assertEqual(data_type(None), 'no value')

    def test_return_when_argument_is_string(self):
        self.assertEqual(data_type('hi'), 2)

    def test_return_when_argument_is_bool(self):
        self.assertEqual(data_type(True), True)

    def test_argument_less_than_100 (self):
        self.assertEqual(data_type(5), 'less than 100')

    def test_argument_more_than_100 (self):
        self.assertEqual(data_type(115), 'more than 100')

    def test_argument_equal_to_100 (self):
        self.assertEqual(data_type(100), 'equal than 100')


if __name__ == '__main__':
    unittest.main()
