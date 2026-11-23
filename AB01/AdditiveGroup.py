from AbelianGroup import AbelianGroup, AbelianGroupElement


class AdditiveGroup(AbelianGroup):
    def __init__(self, R):  # R ist ein Ring
        self.R = R

    def identity(self):
        return AdditiveGroupElement(self.R.zero())

    def enum(self):
        return [AdditiveGroupElement(r) for r in self.R.enum()]


class AdditiveGroupElement(AbelianGroupElement):
    def __init__(self, r):  # r ist ein RingElement
        self.r = r

    def multiply(self, other):  # Gruppenoperation ist die Ring-Addition!
        return AdditiveGroupElement(self.r.add(other.r))

    def inverse(self):
        return AdditiveGroupElement(self.r.additive_inverse())

    def identity(self):
        return AdditiveGroupElement(self.r.zero())

    def __eq__(self, other):
        return self.r == other.r
