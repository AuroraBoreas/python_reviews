
from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)


class Knight(Concrete): pass

class Archer(Concrete): pass

class Barrackes: pass