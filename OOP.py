import abc

class SmartPhone:

    def __init__(self, imei, os, processor, memory):
        """
        Initialises SmartPhone

        :param imei:
        :param os:
        :param processor:
        :param memory:
        """
        self.__imei = imei # private field (Encapsulation)
        self.os = os
        self.processor = processor
        self.memory = memory

    def make_call(self, number):
        if not isinstance(number, int):
            raise TypeError('number should be integer')
        else:
            return 'Dialing {}'.format(number)

    def install_app(self, app_name):
        return '%s has been installed' %app_name

    def update_os(self, update_url):
        return 'updating from server %s' %update_url

    @abc.abstractmethod
    def bluetooth(self, *other_devices):
        """Must be implemented by subclass"""
        raise NotImplemented('Method must be implemented by subclass')


# Iphone inherits from SmartPhone
class Iphone(SmartPhone):

    def __init__(self, imei, os, processor, memory, size, color, version, price):
        super().__init__(imei, os, processor, memory) # Call to the super class constructor
        self.size = size
        self.color = color
        self.version = version
        self.price = price

    def install_app(self, app_name):
        """
        Overrides install_app method from Parent class
        :param app_name:
        :return:
        """
        return 'Installing %s from the app store' %app_name # Polymorphism

    # Start camera in mode given, or default if none given
    def start_camera(self, mode = None):
        """
        This depicts method overloading in Python.
        :param mode:
        :return:
        """
        if mode != None:
            return 'Camera started in %s mode' %mode
        else:
            return 'Camera started in default mode'

    def bluetooth(self, *other_devices):
        """
        Implement abstract parent class method

        :param other_devices:
        :return:
        """
        return 'Paired with {}'.format(" ".join(other_devices))

