# Visitor - double dispatch - method overloading 
from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor:
    def visit(self, d:Dot)->None:
        print(f'{self.__class__} visited dot({d})')
        
    def visit(self, s:Shape)->None:
        print(f'{self.__class__} visited shape({s})')

class Graphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor)->None:
        v.visit(self)

class Shape(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Dot(Graphic):
    def accept(self, v: Visitor) -> None:
        v.visit(self)