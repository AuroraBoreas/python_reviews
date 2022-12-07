"#" 
from __future__ import annotations
from typing import overload


class Visitor:
    @overload
    def visit(self, d:Dot) -> None:
        print(f'{self.__class__} visited {d.__class__}')
    @overload
    def visit(self, s:Shape) -> None:
        print(f'{self.__class__} visited {s.__class__}')

class Figure:
    def accept(self, v:Visitor) -> None:
        raise NotImplementedError()

class Shape(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Dot(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)