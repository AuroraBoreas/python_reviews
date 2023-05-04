"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload

class Figure(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class Dot(Figure):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)

class Shape(Figure):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)

class Visitor:
    @overload
    def visit(self, d: Dot) -> None: ...
    
    @overload
    def visit(self, s: Shape) -> None:...

    def visit(self, f: Dot | Shape) -> None:
        print(f"{self.__class__.__qualname__} visited {f.__class__.__qualname__}")

def client_code() -> None:
    d1: Dot = Dot()
    s1: Shape = Shape()
    v: Visitor = Visitor()
    d1.accept(v)
    s1.accept(v)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()