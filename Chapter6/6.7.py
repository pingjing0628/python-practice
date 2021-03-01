class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    # 6.7
    def __str__(self):
        return 'name: {}, symbol: {}, number: {}'.format(self.name, self.symbol, self.number)


example = Element('Hydrogen', 'H', 1)

dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**dict1)

print(hydrogen)

