# 

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class IGraph(ABC):
    @abstractmethod
    def accept(self, v:Visitor) -> None: pass

class Dot(IGraph):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Shape(IGraph):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Visitor:
    @overload
    def visit(self, d:Dot) -> None:
        print(f'{self.__class__} visited {d.__class__}')

    def visit(self, s:Shape) -> None:
        print(f'{self.__class__} visited {s.__class__}')