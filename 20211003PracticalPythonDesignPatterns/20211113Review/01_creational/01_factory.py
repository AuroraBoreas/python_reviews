# input a string, return an object

from abc import ABC, abstractmethod


class Shape:
    def draw(self)->None: pass

class Circle(Shape):
    def draw(self) -> None:
        print(f'{self.__class__}, start drawing..')

class Square(Shape):
    def draw(self) -> None:
        print(f'{self.__class__}, start drawing..')

class Factory(ABC):
    @abstractmethod
    def make_object(self)->Shape:
        pass

class CircleFactory(Factory):
    def make_object(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> Shape:
        return Square()

def client_code(f:Factory)->None:
    drawable = f.make_object()
    drawable.draw()
