# 
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
        self.assets:List[Any] = []

    def __str__(self) -> str:
        return f'{self!r}, {self.assets}'

    def clone(self) -> object:
        return copy.deepcopy(self)