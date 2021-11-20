from __future__ import annotations
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, List

class Prototype(ABC):
    @abstractmethod
    def clone(self)->object:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets:List[Any] = []

    def clone(self) -> object:
        return deepcopy(self)

    def __str__(self) -> str:
        return '{0!r}, {1}'.format(self, ', '.join(map(str, self.assets)), end='')
