"prototype: robot must have a prototype;" 

from abc import ABCMeta
import copy
from typing import List


class Prototype(metaclass=ABCMeta):
    def clone(self)->object: raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deep_copy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._val:List[int] = []
    def __str__(self) -> str:
        return f'{self!r} : {self._val}'
    def clone(self) -> object:
        return copy.deepcopy(self)