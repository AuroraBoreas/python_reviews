"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self) -> str:
        raise NotImplementedError()

class Circle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} : start drawing..'

class Rectangle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} : start drawing..'

class Factory(metaclass=ABCMeta):
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
    drawable:Shape = f.drawable()
    print(drawable.draw())