"#" 

from __future__ import annotations
from abc import abstractmethod
from typing import overload


class Vistor:
    @overload
    def visit(self, s:Shape) -> None:
        print(f'{self.__class__} visited {s}')
    
    def visit(self, d:Dot) -> None:
        print(f'{self.__class__} visited {d}')

class Figure:
    @abstractmethod
    def accept(self, visitor:Vistor) -> None:
        pass

class Shape(Figure):
    def accept(self, visitor: Vistor) -> None:
        visitor.visit(self)

class Dot(Figure):
    def accept(self, visitor: Vistor) -> None:
        visitor.visit(self)