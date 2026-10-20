from AbelianGroup import AbelianGroup
from UnitGroupElement import UnitGroupElement


class UnitGroup(AbelianGroup):
    def __init__(self, R):  # R ist ein Ring
        self.R = R

    def identity(self):
        return UnitGroupElement(self.R.one())

    def enum(self):
        units = [r for r in self.R.enum() if r.is_unit()]
        return [UnitGroupElement(r) for r in units]
