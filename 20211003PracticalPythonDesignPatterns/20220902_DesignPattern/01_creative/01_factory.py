"#" 

from abc import ABC, abstractmethod
from typing import List


class Shape:
    def draw(self) -> str:
        raise NotImplementedError()

class Circle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} starts drawing..'

class Rectangle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} starts drawing..'

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

def client_code(f:Factory) -> None:
    d:Shape = f.drawable()
    print(d.draw())

if __name__ == '__main__':
    factories:List[Factory] = [
        CircleFactory(),
        RectangleFactory(),
    ]

    for factory in factories:
        client_code(factory)