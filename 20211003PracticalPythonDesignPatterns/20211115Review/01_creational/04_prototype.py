# clone 

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object:
        pass

class Concrete(Prototype):
    def clone(self) -> object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets:List[Any] = []

    def __str__(self)->str:
        return '{}'.format(', '.join(map(str, self.assets)), end='')

def client_code()->None:
    k1 = Knight()
    k1.assets.append(1)
    print('k1: ', k1)

    k2:Knight = k1.clone()
    k2.assets.append([1, 2])
    print('k1: ', k1)
    print('k2: ', k2)