"#" 

from abc import ABC, abstractmethod


class Shape:
    def draw(self) -> str:
        raise NotImplementedError()

class Circle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} starts drawing..'

class Square(Shape):
    def draw(self) -> str:
        return f'{self.__class__} starts drawing..'  

class Factory(ABC):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError()

class CircleFactory(Factory):
    def drawable(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def drawable(self) -> Shape:
        return Square()

def client_code(f:Factory) -> None:
    d = f.drawable()
    print(d.draw())
