import unittest
from fizz_buzz import fizz_buzz


class Test(unittest.TestCase):
    """Unit test cases for fizz_buzz"""

    def test_non_int_arg_type(self):
        self.assertEqual(fizz_buzz('hello'), 'Invalid Argument',
                         msg='should return Invalid '
                             'Argument for non integer args')

    def test_arg_less_than_one(self):
        self.assertEqual(fizz_buzz(0), 'Invalid Argument',
                         msg='should return Invalid '
                             'Argument for 0 and negatives')

    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), 'fizz',
                         msg='should return `fizz` for '
                             'number divisible by 3')

    def test_buzz(self):
        self.assertEqual(fizz_buzz(5), 'buzz',
                         msg='should return `buzz` for '
                             'number divisible by 5')

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15), 'fizzBuzz',
                         msg='should return `fizzBuzz` '
                             'for number divisible by 5 and 3')

    def test_not_fizz_or_buzz(self):
        self.assertEqual(fizz_buzz(1), 1,
                         msg='should return the input value if'
                             ' NOT multiple of 3 or 5')


if __name__ == '__main__':
    unittest.main()
