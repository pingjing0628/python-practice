class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'


bb = Bear()
rr = Rabbit()
oo = Octothorpe()

print(bb.eats())
print(rr.eats())
print(oo.eats())
