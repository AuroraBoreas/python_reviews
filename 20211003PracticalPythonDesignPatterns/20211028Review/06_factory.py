# factory

from abc import ABCMeta, abstractmethod


class Shape:
    def __init__(self) -> None: pass
    def draw(self)->None: pass

class Square(Shape):
    def __init__(self) -> None:
        super().__init__()

    def draw(self) -> None:
        print('draw a square..')

class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()

    def draw(self) -> None:
        print('draw a circle..')

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_object(self)->Shape: pass

class CircleFactory(Factory):
    def make_object(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> Shape:
        return Square()

def client_code(factory:Factory)->None:
    drawable = factory.make_object()
    drawable.draw()

