# 

from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self)->None:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> None:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.val:str = None

    def __str__(self) -> str:
        return f'{self!r}, {self.val}'

    def clone(self) -> None:
        return copy.deepcopy(self)