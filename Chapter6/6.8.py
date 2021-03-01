class Element():
    def __init__(self, name, symbol, number):
        # __name 為私用
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
example = Element(**dict1)
print(example.name)

