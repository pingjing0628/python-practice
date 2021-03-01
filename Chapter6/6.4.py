class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    # 6.6
    def dump(self):
        print('name: {}, symbol: {}, number: {}'.format(self.name, self.symbol, self.number))


example = Element('Hydrogen', 'H', 1)

# 6.5
dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**dict1)

print(hydrogen.name)

# 6.6
print(hydrogen.dump())
