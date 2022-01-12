# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.val:Any = None

    def __str__(self) -> str:
        return f'{self!r}, {self.val}'

    def clone(self) -> object:
        return copy.deepcopy(self)