from abc import ABC, abstractmethod

from AdditiveGroup import AdditiveGroup
from UnitGroup import UnitGroup


class Ring(ABC):
    # Ein endlicher kommutativer Ring (R, +, *, 0, 1).
    @abstractmethod
    def zero(self):
        # Das Nullelement 0.
        pass

    @abstractmethod
    def one(self):
        # Das Einselement 1.
        pass

    @abstractmethod
    def enum(self):
        # Liste aller Elemente von R.
        pass

    def get_additive_group(self):
        return AdditiveGroup(self)

    def units(self):
        return UnitGroup(self)