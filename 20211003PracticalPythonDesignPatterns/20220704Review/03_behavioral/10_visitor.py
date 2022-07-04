"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class Visitor:
    @overload
    def visit(self, d:Dot) -> None:
        print(f'{self.__class__} visited {d.__class__}')

    def visit(self, o:Shape) -> None:
        print(f'{self.__class__} visited {o.__class__}')

class IGraphic(ABC):
    @abstractmethod
    def accept(self, v:Visitor) -> None:
        pass

class Shape:
    def accept(self, v:Visitor) -> None:
        v.visit(self)

class Dot:
    def accept(self, v:Visitor) -> None:
        v.visit(self)