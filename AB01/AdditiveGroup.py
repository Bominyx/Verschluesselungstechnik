from AbelianGroup import AbelianGroup
from AdditiveGroupElement import AdditiveGroupElement


class AdditiveGroup(AbelianGroup):
    def __init__(self, R):  # R ist ein Ring
        self.R = R

    def identity(self):
        return AdditiveGroupElement(self.R.zero())

    def enum(self):
        return [AdditiveGroupElement(r) for r in self.R.enum()]
