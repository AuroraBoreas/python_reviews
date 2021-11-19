# visitor - double dispatch(method overloaind)
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class Graphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor)->None:
        raise NotImplementedError()

class Dot(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Shape(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Visitor:
    @overload
    def visit(d:Dot)->None:
        print('visited dot;')

    def visit(s:Shape)->None:
        print('visited shape;')