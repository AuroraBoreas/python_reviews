"#" 

from abc import ABC, abstractmethod
import copy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> object:
        pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._val:List[Any] = []

    def add(self, e:Any) -> None:
        self._val.append(e)

    def __str__(self) -> str:
        return f'{self.__class__} {self._val}'

    def clone(self) -> object:
        return copy.deepcopy(self)