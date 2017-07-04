import unittest
from data_types import data_type

class Datatype(unittest.TestCase):
    def test_return_when_argument_is_none(self):
        self.assertEqual(data_types(None), 'no value')

    def test_return_when_argument_is_string(self):
        self.assertEqual(data_types('hi'), 2)

    def test_return_when_argument_is_bool(self):
        self.assertEqual(data_types(True), True)


if __name__ == '__main__':
    unittest.main()
