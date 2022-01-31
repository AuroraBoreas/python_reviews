
from abc import ABCMeta, abstractmethod
import copy
from typing import Any, List

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self)->object: pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.val:List[Any] = []

    def __str__(self) -> str:
        return f'{self.__class__}, {self.val}'

    def clone(self) -> object:
        return copy.deepcopy(self)
