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
