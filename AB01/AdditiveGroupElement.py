from AbelianGroupElement import AbelianGroupElement


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
