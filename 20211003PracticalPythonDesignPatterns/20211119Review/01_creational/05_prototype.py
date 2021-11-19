# clone 

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object: pass

class Concrete(Prototype):
    def clone(self) -> object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets:List[Any] = []

    def clone(self) -> object:
        return deepcopy(self)

    def __str__(self) -> str:
        return '{}'.format(', '.join(map(str, self.assets)), end='')