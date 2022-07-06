# give a string and return an object 

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self) -> str:
        raise NotImplementedError()

class Circle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} starts drawing..'

class Rectangle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} starts drawing..'

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
    drawable = f.drawable()
    print(drawable.draw())