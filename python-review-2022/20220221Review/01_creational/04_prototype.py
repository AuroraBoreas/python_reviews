# 

from abc import ABC, abstractmethod
import copy
from typing import List


class Prototype(ABC):
    @abstractmethod
    def clone(self)->object: pass

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Prototype):
    def __init__(self) -> None:
        self.val:List[int] = []

    def __str__(self) -> str:
        return f'{self!r} : {self.val}'

    def clone(self) -> object:
        return copy.deepcopy(self)