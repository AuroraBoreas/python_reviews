#
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class Visitor:
    @overload
    def visit(self, d:Dot) -> None:
        print(f'{d.__class__} visited')

    def visit(self, s:Shape) -> None:
        print(f'{s.__class__} visited')

class Figure(ABC):
    @abstractmethod
    def accept(self, v:Visitor) -> None:
        raise NotImplementedError()

class Dot(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Shape(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)