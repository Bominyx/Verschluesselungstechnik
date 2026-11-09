from Ring import Ring
from RingElement import RingElement
from Zn import ZnElement


class PairRing(Ring):
    def __init__(self, p=3, c=2):
        self.p = p
        self.c = c.value if isinstance(c, ZnElement) else c

    def zero(self):
        return PairElement(0, 0, self.p, self.c)

    def one(self):
        return PairElement(1, 0, self.p, self.c)

    def enum(self):
        elements = []
        for i in range(self.p):
            for j in range(self.p):
                elements.append(PairElement(i, j, self.p, self.c))
        return elements


class PairElement(RingElement):
    def __init__(self, x, y, p=3, c=2):
        self.x = x if isinstance(x, ZnElement) else ZnElement(x, p)
        self.y = y if isinstance(y, ZnElement) else ZnElement(y, p)
        self.n = p  # if isinstance(p, ZnElement) else ZnElement(p, p)
        self.c = c if isinstance(c, ZnElement) else ZnElement(c, p)

    def add(self, other):
        return PairElement(self.x.add(other.x), self.y.add(other.y), self.n, self.c)

    def multiply(self, other):
        return PairElement(self.x.multiply(other.x).add(self.c.multiply(self.y.multiply(other.y))),
                           self.x.multiply(other.y).add(other.x.multiply(self.y)), self.n, self.c)

    def additive_inverse(self):
        return PairElement(self.x.additive_inverse(), self.y.additive_inverse(), self.n, self.c)

    def zero(self):
        return PairElement(0, 0, self.n, self.c)

    def one(self):
        return PairElement(1, 0, self.n, self.c)

    def ring(self):
        return PairRing(self.n, self.c)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.n == other.n and self.c == other.c

    def __repr__(self) -> str:
        return f"({str(self.x)}, {str(self.y)})"
