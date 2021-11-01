# prototype

from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self): pass

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets = []
        super().__init__()

    def clone(self):
        return deepcopy(self)

if __name__ == '__main__':
    k1 = Knight()
    k1.assets.append(1)
    k2 = k1.clone()
    k2.assets.append(2)
    print('{0!r} : {0}'.format(k1.assets))
    print('{0!r} : {0}'.format(k2.assets))