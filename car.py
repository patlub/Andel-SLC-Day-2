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
