from AbelianGroupElement import AbelianGroupElement


class UnitGroupElement(AbelianGroupElement):
    def __init__(self, r):  # r ist ein RingElement und eine Einheit
        self.r = r

    def multiply(self, other):
        return UnitGroupElement(self.r.multiply(other.r))

    def identity(self):
        return UnitGroupElement(self.r.one())

    def inverse(self):
        return UnitGroupElement(self.r.inverse())  # noch zu klaeren!

    def __eq__(self, other):
        return self.r == other.r

    def __repr__(self):
        return str(self.r)  # damit print() den Wert lesbar ausgibt
