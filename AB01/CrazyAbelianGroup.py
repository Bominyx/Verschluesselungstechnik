from Zn import ZnElement
from AbelianGroup import AbelianGroup, AbelianGroupElement


class CrazyAbelianGroup(AbelianGroup):
    def __init__(self, R):  # R ist ein Ring
        self.R = R

    def identity(self):
        return CrazyGroupElement(self.R.zero(), self.R.n)

    def enum(self):
        elements = [CrazyGroupElement(r, self.R.n) for r in self.R.enum()]
        elements.append(CrazyGroupElement(0, self.R.n, True))
        return elements


class CrazyGroupElement(AbelianGroupElement):
    def __init__(self, x, p, is_infinite=False):
        self.x = x if isinstance(x, ZnElement) else ZnElement(x, p)
        self.is_infinite = is_infinite

    def multiply(self, other):  # Gruppenoperation
        if self.is_infinite and other.is_infinite:
            return CrazyGroupElement(self.x.zero(), self.x.n)

        if self.is_infinite:
            if other.x == other.x.zero():
                return CrazyGroupElement(self.x.zero(), self.x.n, True)
            return CrazyGroupElement(self.x.one().additive_inverse().multiply(other.x.inverse()), self.x.n)

        if other.is_infinite:
            if self.x == self.x.zero():
                return CrazyGroupElement(self.x.zero(), self.x.n, True)
            return CrazyGroupElement(self.x.one().additive_inverse().multiply(self.x.inverse()), self.x.n)

        xy = self.x.multiply(other.x)
        if xy == xy.one():
            return CrazyGroupElement(self.x.zero(), self.x.n, True)

        return CrazyGroupElement(self.x.one().subtract(xy).inverse().multiply(self.x.add(other.x)), self.x.n)

    def inverse(self):
        return CrazyGroupElement(self.x.additive_inverse(), self.x.n, self.is_infinite)

    def identity(self):
        return CrazyGroupElement(self.x.zero(), self.x.n)

    def __eq__(self, other):
        return (self.x == other.x) and (self.is_infinite == other.is_infinite)

    def __repr__(self):
        return str(self.x) if not self.is_infinite else "inf"
