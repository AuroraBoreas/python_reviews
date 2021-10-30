# robot

from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self): raise NotImplementedError()

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self):
        self.assets = [1, 2, 3, [1, 2]]

    def clone(self):
        return deepcopy(self)

if __name__ == '__main__':
    k1 = Knight()
    k2 = k1.clone()
    print(k1.assets == k2.assets)
    print(k1.assets is k2.assets)
