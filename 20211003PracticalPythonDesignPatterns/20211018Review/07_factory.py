# factory

from abc import ABCMeta, abstractmethod


class Shape:
    def __init__(self): pass

    def draw(self)->None: pass

class Circle(Shape):
    def draw(self)->None:
        print('drawing a cicle...')

class Square(Shape):
    def draw(self)->None:
        print('drawing a square...')

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_object(self)->Shape: raise NotImplementedError()

class CircleFactory(Factory):
    def make_object(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> Shape:
        return Square()

def client_code(factory:Factory)->None:
    drawable = factory.make_object()
    drawable.draw()

if __name__ == '__main__':
    s = SquareFactory()
    c = CircleFactory()

    client_code(s)
    client_code(c)