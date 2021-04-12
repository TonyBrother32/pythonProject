from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @property
    @abstractmethod
    def material(self):
        pass

    def __add__(self, other):
        return self.material + other.material

    def __str__(self):
        return self.material


class Coat(Clothes):
    @property
    def material(self):
        return float(self.value/6.5 + 0.5)


class Suit(Clothes):
    @property
    def material(self):
        return float(2*self.value/100 + 0.3)


coat = Coat(52)
suit = Suit(180)
print(f"Расход ткани составил {coat + suit}м")
