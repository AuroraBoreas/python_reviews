# visitor - double display -> method overloading;
# python does not support method overloading; see C++ implementation;
# note: in C++ implementation, pitfall: "circular dependency"; using "forward declaration" to avoid

from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Visitor:
    def visit(s:Shape)->None:
        print('visited shape')

    def visit(d:Dot)->None:
        print('visited dot')

class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v:Visitor)->None:
        pass

class Shape(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Dot(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)