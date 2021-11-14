# visitor
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import overload

class IGraphic(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v: Visitor)->None:
        pass

class Shape(IGraphic):
    def accept(self, v: Visitor) -> None:
        return v.visit(self)

class Dot(IGraphic):
    def accept(self, v: Visitor) -> None:
        return v.visit(self)

class Visitor:
    @overload
    def visit(self, s:Shape)->None:
        print('visited shape')
    
    def visit(self, d:Dot)->None:
        print('visited dot')