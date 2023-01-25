from __future__ import annotations
from abc import abstractmethod
from typing import overload


class Figure:
    @abstractmethod
    def accept(self, v: Visitor) -> None:
        raise NotImplementedError

class Dot(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Shape(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Visitor:
    @overload
    def visit(self, d: Dot) -> None: ...

    @overload
    def visit(self, s: Shape) -> None: ...

    def visit(self, f: Dot | Shape) -> None:
        print(f"{self.__class__} visited {f.__class__}")
