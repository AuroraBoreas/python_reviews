# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class IGraphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor)->None: pass

class Dot(IGraphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Shape(IGraphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Visitor:
    @overload
    def visit(self, d:Dot)->None:
        print(f'{self.__class__} visited {d}')

    def visit(self, s:Shape)->None:
        print(f'{self.__class__} visited {s}')