

class Gem:
    amount = 0

    def __init__(self, name="Unknown", weight=None, prise=None, colour="Unknown", shape="Unknown"):
        self.__name = name
        self.__weight = weight
        self.__price = prise
        self.__colour = colour
        self.__shape = shape
        Gem.amount = Gem.amount + 1

    def to_string(self):
        return "Name: {}, weight: {}, colour: {}, shape: {}, price: {}".format(self.__name,
                                                                               self.__weight,
                                                                               self.__colour,
                                                                               self.__shape,
                                                                               self.__price)

    @staticmethod
    def print_static_sum():
        print("Gems amount: {}".format(Gem.amount))

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price

    def get_colour(self):
        return self.__colour

    def get_shape(self):
        return self.__shape

    def set_name(self, name):
        self.__name = name

    def set_weight(self, weight):
        self.__weight = weight

    def set_prise(self, prise):
        self.__price = prise

    def set_colour(self, colour):
        self.__colour = colour

    def set_shape(self, shape):
        self.__shape = shape


stone = Gem("Stone", 4, 4, "blue")
print(stone.to_string())
another_stone = Gem()
print(another_stone.to_string())
whatever_stone = Gem("Stone", 25, 11, "red", "round")
print(whatever_stone.to_string())
Gem.print_static_sum()
