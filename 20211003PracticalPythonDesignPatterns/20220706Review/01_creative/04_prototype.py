# 
from abc import ABC, abstractmethod
from typing import List
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> object:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._val:List[int] = []

    def add(self, item:int) -> None:
        self._val.append(item)
    
    def clone(self) -> object:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f'{self.__class__} : {self._val}'

def client_code() -> None:
    k1 = Knight()
    k1.add(1); k1.add(2)
    k2 = k1.clone()
    k2.add(3)
    print(k1)
    print(k2)

if __name__ == '__main__':
    client_code()