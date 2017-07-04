class Car(object):
    """
    Class to represent a car object
    Attributes:
        name: name of car
        model: car model
        type: car type
    """

    def __init__(self, name="General", model="GM", type="saloon"):
        """
        initialises Car with default values for name, model and type

        :param name:
        :param model:
        :param type:
        """
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0

    @property
    def num_of_doors(self):
        """Return number of doors"""
        if self.name == "Porshe" or self.name == "Koenigsegg":
            return 2
        return 4

    @property
    def num_of_wheels(self):
        """Return number of wheels"""
        if self.type != "trailer":
            return 4
        return 8

    def is_saloon(self):
        """Return car type"""
        if self.type == "saloon":
            return True
        return False
