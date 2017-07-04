import unittest
from OOP import SmartPhone, Iphone

class OOPTestCase(unittest.TestCase):
    def test_creation_of_smartphone(self):
        smartphone  = SmartPhone('EJNJEEE87','ios7', 'intel', '8gb')
        self.assertTrue(isinstance(smartphone, SmartPhone))

    def test_make_call_of_smartphone(self):
        smartphone  = SmartPhone('EJNJEEE87','ios7', 'intel', '8gb')
        self.assertEqual(smartphone.make_call(777555), 'Dialing 777555')

    def test_creation_of_iphone(self):
        iphone  = Iphone('HSJSSK333', 'ios8', 'apple', '4gb','4inches', 'black', '9.0', 1000)
        self.assertTrue(isinstance(iphone, SmartPhone))


if __name__ == '__main__':
    unittest.main()
