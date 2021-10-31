# visitor
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Visitor:
    def visit(self, s:Shape):
        print('visited shape')

    def visit(self, d:Dot):
        print('visited dot')

class IGraphic(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v:Visitor)->None: pass

class Shape(IGraphic):
    def accept(self, v:Visitor) -> None:
        v.visit(self)

class Dot(IGraphic):
    def accept(self, v:Visitor) -> None:
        v.visit(self)