"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class Shape:
    def draw(self) -> str:
        raise NotImplementedError()

class Circle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing.."

class Rectangle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing.."

class Factory(ABC):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError()

class CircleFactory(Factory):
    def drawable(self) -> Shape:
        return Circle()

class RectangleFactory(Factory):
    def drawable(self) -> Shape:
        return Rectangle()

def client_code(f: Factory) -> None:
    s1: Shape = f.drawable()
    logging.info(s1.draw())

def main() -> None:
    for f in [
        CircleFactory(),
        RectangleFactory()
    ]:
        client_code(f)

if __name__ == '__main__':
    main()