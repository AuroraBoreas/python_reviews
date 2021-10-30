# clone

from abc import ABCMeta, abstractmethod
from copy import deepcopy
from typing import Any, List

class Prototype:
    __metaclass__ = ABCMeta
    @abstractmethod
    def clone(self)->object: pass


class Concrete(Prototype):
    def clone(self)->object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self):
        self.assets:List[Any] = []

    def clone(self)->object:
        return deepcopy(self)

def client_code():
    k1 = Knight()
    k1.assets.append(1)
    print(k1.assets)

    k2 = k1.clone()
    k2.assets.append(2)
    print(k1.assets)
    print(k2.assets)

if __name__ == '__main__':
    client_code()
