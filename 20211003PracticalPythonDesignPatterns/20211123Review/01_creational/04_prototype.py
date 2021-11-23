# 

from abc import ABC, abstractmethod
import copy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object:
        pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets:List[Any] = []

    def clone(self) -> object:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f'{self!r}, {self.assets}'