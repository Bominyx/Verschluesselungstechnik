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


class RingElement(ABC):
    # Ein Element x eines Rings.
    @abstractmethod
    def add(self, other):  # x + y
        pass

    @abstractmethod
    def multiply(self, other):  # x * y
        pass

    @abstractmethod
    def additive_inverse(self):  # -x
        pass

    @abstractmethod
    def zero(self):  # das Nullelement des Rings von x
        pass

    @abstractmethod
    def one(self):  # das Einselement des Rings von x
        pass

    @abstractmethod
    def ring(self):  # der Ring R, zu dem x gehoert
        pass

    def subtract(self, other):
        # Berechnet x-y := x + (-y).
        return self.add(other.additive_inverse())

    def is_unit(self):
        # Prueft, ob x eine Einheit ist: Gibt es ein y mit x * y = 1?
        one = self.one()
        for y in self.ring().enum():
            if self.multiply(y) == one:
                return True
        return False

    def inverse(self):
        # Das multiplikative Inverse x^(-1), falls x eine Einheit ist.
        one = self.one()
        for y in self.ring().enum():
            if self.multiply(y) == one:
                return y
        raise ValueError("Das Element ist keine Einheit.")
