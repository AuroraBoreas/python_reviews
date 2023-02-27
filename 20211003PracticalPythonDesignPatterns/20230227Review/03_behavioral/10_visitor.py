# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import overload


class Figure(ABC):
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
        print(f'{self.__class__.__name__} visited {f.__class__.__name__}')

def client_code() -> None:
    v: Visitor = Visitor()
    for f in [
        Dot(),
        Shape(),
    ]:
        f.accept(v)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()


