"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
import copy
from abc import ABC, abstractmethod
from typing import Any


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> object:
        pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._attr = []

    def add(self, attribute:Any) -> None:
        self._attr.append(attribute)

    def clone(self) -> object:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f'{self.__annotations__} : {self._attr}'

def client_code() -> None:
    k1 = Knight()
    k1.add(1)
    k2 = k1.clone()
    k1.add(2)
    print(k1)
    print(k2)

if __name__ == '__main__':
    client_code()
