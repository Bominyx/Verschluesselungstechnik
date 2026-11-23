from AbelianGroup import AbelianGroup, AbelianGroupElement


class UnitGroup(AbelianGroup):
    def __init__(self, R):  # R ist ein Ring
        self.R = R

    def identity(self):
        return UnitGroupElement(self.R.one())

    def enum(self):
        units = [r for r in self.R.enum() if r.is_unit()]
        return [UnitGroupElement(r) for r in units]


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
