# clone
from __future__ import annotations
from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):
    @abstractmethod
    def clone(self): pass

class Concrete(Prototype):
    def clone(self)->Concrete:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self):
        self.assets = []

    def clone(self)->Knight:
        return deepcopy(self)

    def __str__(self)->str:
        return '{0!r}'.format(self)

if __name__ == '__main__':
    k1 = Knight()
    k1.assets.append(1)
    k2 = k1.clone()
    k2.assets.append(2)
    print(k1, k1.assets)
    print(k2, k2.assets)