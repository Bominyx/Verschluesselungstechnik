from math import gcd

from Ring import Ring, RingElement


class Zn(Ring):
    def __init__(self, n: int):
        self.n = n

    def zero(self) -> ZnElement:
        return ZnElement(0, self.n)

    def one(self) -> ZnElement:
        return ZnElement(1, self.n)

    def enum(self) -> list[ZnElement]:
        return [ZnElement(k, self.n) for k in range(self.n)]


class ZnElement(RingElement):
    def __init__(self, value: int, n: int):
        self.n = n
        self.value = value % n  # stets ein Wert in {0, 1, ..., n-1}

    def add(self, other: ZnElement) -> ZnElement:
        return ZnElement(self.value + other.value, self.n)

    def multiply(self, other: ZnElement) -> ZnElement:
        return ZnElement(self.value * other.value, self.n)

    def additive_inverse(self) -> ZnElement:
        return ZnElement(-self.value, self.n)  # (-x) % n liegt in {0,...,n-1}

    def zero(self) -> ZnElement:
        return ZnElement(0, self.n)

    def one(self) -> ZnElement:
        return ZnElement(1, self.n)

    def ring(self) -> Zn:
        return Zn(self.n)

    def __eq__(self, other):
        return self.n == other.n and self.value == other.value

    def __repr__(self):
        return str(self.value)  # damit print() den Wert lesbar ausgibt

    def fast_is_unit(self):
        return gcd(self.value, self.n) == 1

    def fast_inverse(self):
        if not self.fast_is_unit():
            raise ValueError("Das Element ist keine Einheit.")
        return ZnElement(pow(self.value, -1, self.n), self.n)
