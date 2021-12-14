# 

from abc import ABC, abstractmethod
import copy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object: pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._assets:List[Any] = []

    def __str__(self)->str:
        return f'{self.__class__}, {self._assets}'

    def clone(self) -> object:
        return copy.deepcopy(self)