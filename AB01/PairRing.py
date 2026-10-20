from Ring import Ring
from RingElement import RingElement
from Zn import ZnElement


class PairRing(Ring):
    def zero(self):
        return PairElement(0, 0)

    def one(self):
        return PairElement(1, 0)

    def enum(self):
        elements = []
        for i in range(3):
            for j in range(3):
                elements.append(PairElement(i, j))
        return elements


class PairElement(RingElement):
    def __init__(self, x, y):
        self.x = x if isinstance(x, ZnElement) else ZnElement(x, 3)
        self.y = y if isinstance(y, ZnElement) else ZnElement(y, 3)

    def add(self, other):
        return PairElement(self.x.add(other.x), self.y.add(other.y))

    def multiply(self, other):
        return PairElement(self.x.multiply(other.x).subtract(self.y.multiply(other.y)),
                           self.x.multiply(other.y).add(other.x.multiply(self.y)))

    def additive_inverse(self):
        return PairElement(self.x.additive_inverse(), self.y.additive_inverse())

    def zero(self):
        return PairElement(0, 0)

    def one(self):
        return PairElement(1, 0)

    def ring(self):
        return PairRing()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"({str(self.x)}, {str(self.y)})"
