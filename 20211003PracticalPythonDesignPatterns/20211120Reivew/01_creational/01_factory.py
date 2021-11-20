from __future__ import annotations
from abc import abstractmethod, ABCMeta

class Shape:
    def draw(self)->None: pass

class Circle(Shape):
    def draw(self) -> None:
        print(f'{self.__class__} start drawing..')

class Square(Shape):
    def draw(self) -> None:
        print(f'{self.__class__} start drawing..')

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_object(self)->Shape:
        raise NotImplementedError()

class CircleFactory(Factory):
    def make_object(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> Shape:
        return Square()

def client_code(f:Factory)->None:
    d = f.make_object()
    d.draw()
