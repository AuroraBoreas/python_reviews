"#" 
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import overload


class Visitor:
    def visit(self, s:Shape) -> None:
        print(f'{self.__class__} visited {s.__class__}')

    @overload
    def visit(self, d:Dot) -> None:
        print(f'{self.__class__} visited {d.__class__}')

class IGraph(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v:Visitor) -> None:
        raise NotImplementedError()

class Shape(IGraph):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Dot(IGraph):
    def accept(self, v: Visitor) -> None:
        v.visit(self)