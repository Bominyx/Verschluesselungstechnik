from Ring import Ring
from RingElement import RingElement


class Zn(Ring):
    def __init__(self, n):
        self.n = n

    def zero(self):
        return ZnElement(0, self.n)

    def one(self):
        return ZnElement(1, self.n)

    def enum(self):
        return [ZnElement(k, self.n) for k in range(self.n)]


class ZnElement(RingElement):
    def __init__(self, value, n):
        self.n = n
        self.value = value % n  # stets ein Wert in {0, 1, ..., n-1}

    def add(self, other):
        return ZnElement(self.value + other.value, self.n)

    def multiply(self, other):
        return ZnElement(self.value * other.value, self.n)

    def additive_inverse(self):
        return ZnElement(-self.value, self.n)  # (-x) % n liegt in {0,...,n-1}

    def zero(self):
        return ZnElement(0, self.n)

    def one(self):
        return ZnElement(1, self.n)

    def ring(self):
        return Zn(self.n)

    def __eq__(self, other):
        return self.n == other.n and self.value == other.value

    def __repr__(self):
        return str(self.value)  # damit print() den Wert lesbar ausgibt
