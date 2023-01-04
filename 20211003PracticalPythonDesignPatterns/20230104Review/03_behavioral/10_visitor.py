"#" 
from __future__ import annotations

from abc import ABC, abstractmethod
import logging
from typing import overload
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


class Figure(ABC):
    @abstractmethod
    def accept(self, v: Visitor) -> None:
        raise NotImplementedError()

class Dot(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Shape(Figure):
    def accept(self, v: Visitor) -> None:
        v.visit(self)

class Visitor:
    @overload
    def visit(self, f: Dot) -> None: ...

    @overload
    def visit(self, f: Shape) -> None: ...

    def visit(self, f: Dot | Shape) -> None:
        logging.info(f'{self.__class__} visited {f.__class__}')

def client_code(f: Figure) -> None:
    v: Visitor = Visitor()
    f.accept(v)

def main() -> None:
    for f in [
        Dot(),
        Shape(),
        Dot(),
    ]:
        client_code(f)
        
if __name__ == '__main__':
    main()