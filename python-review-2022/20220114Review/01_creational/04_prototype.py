# 

from abc import ABC, abstractmethod
from typing import Any, List
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object: pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Prototype):
    def __init__(self) -> None:
        self.val:List[Any] = []

    def __str__(self) -> str:
        return f'{self!r}, {self.val}'
    
    def clone(self) -> object:
        return copy.deepcopy(self)