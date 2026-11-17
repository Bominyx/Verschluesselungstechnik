from AB01.Zn import ZnElement
from AbelianGroup import AbelianGroup
from AbelianGroupElement import AbelianGroupElement


class CrazyAbelianGroup(AbelianGroup):
    def __init__(self, R, p):  # R ist ein Ring
        self.R = R
        self.p = p

    def identity(self):
        return CrazyGroupElement(self.R.zero(), self.p)

    def enum(self):
        return [CrazyGroupElement(r, self.p) for r in self.R.enum()].append(CrazyGroupElement(0, self.p, True))


class CrazyGroupElement(AbelianGroupElement):
    def __init__(self, x, p, is_infinite=False):
        self.x = x if isinstance(x, ZnElement) else ZnElement(x, p)
        self.is_infinite = is_infinite

    def multiply(self, other):  # Gruppenoperation
        if not self.is_infinite and other.is_infinite and self.x.zero() == self.x:
            return CrazyGroupElement(self.x.zero(), self.x.n, True)

        if self.is_infinite and not other.is_infinite and other.x.zero() == other.x:
            return CrazyGroupElement(self.x.zero(), self.x.n, True)

        if (self.is_infinite and not other.is_infinite) or (not self.is_infinite and other.is_infinite):
            return CrazyGroupElement(self.x.one().additive_inverse().multiply(self.x.inverse()), self.x.n)

        if self.is_infinite and other.is_infinite:
            return CrazyGroupElement(self.x.zero(), self.x.n)

        xy = self.x.multiply(other)
        if xy == xy.one():
            return CrazyGroupElement(self.x.zero(), self.x.n,
                                     True)

        return CrazyGroupElement(self.x.one().subtract(xy).inverse().multiply(self.x.add(other)), self.x.n,
                                 self.is_infinite)

    def inverse(self):
        return CrazyGroupElement(self.x.additive_inverse(), self.x.n, self.is_infinite)

    def identity(self):
        return CrazyGroupElement(self.x.zero(), self.x.n, self.is_infinite)

    def __eq__(self, other):
        return self.x == other.x or self.is_infinite == self.is_infinite
