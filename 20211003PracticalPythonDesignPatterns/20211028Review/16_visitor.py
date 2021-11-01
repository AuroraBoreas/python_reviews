# visitor - double dispatch;

from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor:
    def visit(self, s:Shape)->None:
        print('visited shape')

    def visit(self, d:Dot)->None:
        print('visited dot')

class IGraphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor)->None:
        pass

class Shape(IGraphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Dot(IGraphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

