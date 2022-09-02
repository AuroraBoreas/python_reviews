"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class Visitor:
    @overload
    def visit(self, p:Point) -> None:
        print(f'{self.__class__} visited {p.__class__}')
    
    def visit(self, s:Shape) -> None:
        print(f'{self.__class__} visited {s.__class__}')

class IGraphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor) -> None:
        raise NotImplementedError()

class Point(IGraphic):
    def accept(self, v: Visitor) -> None:
        return v.visit(self)

class Shape(IGraphic):
    def accept(self, v: Visitor) -> None:
        return v.visit(self)