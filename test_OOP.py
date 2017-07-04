import unittest
from OOP import SmartPhone, Iphone, Samsung


class OOPTestCase(unittest.TestCase):
    def setUp(self):
        self.iphone = Iphone('HSJSSK333', 'ios8', 'apple', '4gb', '4inches', 'black', '9.0', 1000)
        self.samsung = Samsung('HSJSSK333', 'ios8', 'apple', '4gb', '4inches', 'black', '9.0', 1000)
        self.smartphone = SmartPhone('EJNJEEE87', 'ios7', 'intel', '8gb')


    def test_creation_of_smartphone(self):
        self.assertTrue(isinstance(self.smartphone, SmartPhone))

    def test_make_call_of_smartphone(self):
        self.assertEqual(self.smartphone.make_call(777555), 'Dialing 777555')

    def test_creation_of_iphone(self):
        self.assertTrue(isinstance(self.iphone, SmartPhone))

    def test_creation_of_Samsung(self):
        self.assertTrue(isinstance(self.samsung, SmartPhone))

    def test_iphone_install_app(self):
        self.assertEqual(self.iphone.install_app('whatsapp'),
                         'Installing whatsapp from the app store')

    def test_samsung_install_app(self):
        self.assertEqual(self.samsung.install_app('facebook'),
                         'Installing facebook from the Google PlayStore')

    def test_phone_phone_start_camera(self):
        self.assertEqual(self.iphone.start_camera(),
                         'Camera started in default mode')

    def test_phone_phone_start_camera_in_mode(self):
        self.assertEqual(self.iphone.start_camera('selfie'),
                         'Camera started in selfie mode')

    def test_iphone_blue_tooth_with_non_Iphone(self):
        self.assertEqual(self.iphone.bluetooth(self.samsung),
                         'Only pairs with fellow Iphone')

    def test_iphone_blue_tooth_with_fellow_Iphone(self):
        self.assertEqual(self.iphone.bluetooth(self.iphone),
                         'Successfully Paired')

    def test_samsung_blue_tooth_with_any_Iphone(self):
        self.assertEqual(self.samsung.bluetooth(self.iphone),
                         'Success. Pairs with any other phone')
        self.assertEqual(self.samsung.bluetooth(self.samsung),
                         'Success. Pairs with any other phone')


if __name__ == '__main__':
    unittest.main()
