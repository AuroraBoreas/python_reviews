
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from typing import Any

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self)->Any: raise NotImplementedError()

class Concrete(Prototype):
    def clone(self)->Any:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self)->None: pass

    def __str__(self)->str: return

    def clone(self) -> Any:
        return deepcopy(self)