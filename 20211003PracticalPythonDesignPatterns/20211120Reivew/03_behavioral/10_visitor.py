from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload

class Graphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor)->None:
        pass

class Shape(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Dot(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Visitor:
    @overload
    def visit(self, s:Shape)->None:
        print(f'{self.__class__} visited shape;')

    def visit(self, d:Dot)->None:
        print(f'{self.__class__} visited dot;')
