# 

from abc import ABC, abstractmethod
import copy
from typing import Self


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        raise NotImplementedError
    
class Concrete(Prototype):
    def clone(self) -> Self:
        return copy.deepcopy(self)
    
class Knight(Concrete):
    def __init__(self) -> None:
        self._vals: list[int] = list()

    def add(self, val: int) -> None:
        self._vals.append(val)

    def clone(self) -> Self:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f'{self.__class__}: {self._vals}'