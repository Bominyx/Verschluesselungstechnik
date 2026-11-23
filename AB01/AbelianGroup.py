from abc import ABC, abstractmethod


class AbelianGroup(ABC):
    # Eine (endliche) abelsche Gruppe (G, *, 1).
    @abstractmethod
    def identity(self):
        # Das neutrale Element 1 von G.
        pass

    @abstractmethod
    def enum(self):
        # Liste aller Elemente von G (nur fuer endliche G moeglich).
        pass

    def order(self):
        # Die Ordnung #G, also die Anzahl der Elemente.
        return len(self.enum())


class AbelianGroupElement(ABC):
    # Ein Element x einer abelschen Gruppe.

    @abstractmethod
    def multiply(self, other):
        pass  # Berechnet x * y.

    @abstractmethod
    def inverse(self):
        pass  # Berechnet x^(-1).

    @abstractmethod
    def identity(self):
        pass  # Das neutrale Element der Gruppe von x.

    def power(self, n):
        # Berechnet x^n fuer eine ganze Zahl n.
        if n < 0:
            return self.inverse().power(-n)
        result = self.identity()
        for _ in range(n):
            result = result.multiply(self)
        return result
