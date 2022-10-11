# 

from abc import ABC, abstractmethod
import copy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> object:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._vals:List[Any] = list()

    def add(self, val:Any) -> None:
        self._vals.append(val)

    def __str__(self) -> str:
        return f'{self.__class__} : {self._vals}'

def client_code() -> None:
    k1: Knight = Knight()
    k1.add(1)
    k1.add(2)
    print(k1,sep='\n\n')
    k2: Knight = k1.clone()
    k1.add(3)
    print(k1)
    print(k2)

if __name__ == '__main__':
    client_code()