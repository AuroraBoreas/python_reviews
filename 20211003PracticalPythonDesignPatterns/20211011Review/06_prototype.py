from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self)->object:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self):
        self.val = None

    @property
    def value(self):
        return self.val

    @value.setter
    def value(self, val:int):
        self.val = val

    def __str__(self): return

    def clone(self) -> object:
        return deepcopy(self)

if __name__ == '__main__':
    k1 = Knight()
    k2 = k1.clone()
    k1.val = 1
    print(k2.val)
    print(k1.val)
