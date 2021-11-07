# clone

from abc import ABCMeta, abstractmethod
from typing import Any
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self)->Any: pass

class Concrete(Prototype):
    def clone(self) -> Any:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets = []

    def clone(self) -> Any:
        return deepcopy(self)

    def __str__(self)->str:
        return f'{self.assets}'

def client_code()->None:
    k1 = Knight()
    k1.assets.append(1)
    print(k1)

    k2 = k1.clone()
    k2.assets.append([1, 2])
    print(k1)
    print(k2)

if __name__ == '__main__':
    client_code()