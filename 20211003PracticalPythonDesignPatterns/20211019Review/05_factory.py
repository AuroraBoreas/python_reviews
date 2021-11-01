# factory

from abc import ABCMeta, abstractclassmethod, abstractmethod


class Shape:
    def __init__(self): pass
    def draw(self)->None:
        raise NotImplementedError()

class Circle(Shape):
    def __init__(self): pass 
    def draw(self) -> None:
        return 'drawing a circle..'

class Square(Shape):
    def __init__(self): pass
    def draw(self) -> None:
        return 'drawing a square..'

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_object(self):
        raise NotImplementedError()

class CircleFactory(Factory):
    def make_object(self):
        return Circle()

class SquareFactory(Factory):
    def make_object(self):
        return Square()

def client_code(factory:Factory)->None:
    drawable = factory.make_object()
    drawable.draw()

if __name__ == '__main__':
    s = SquareFactory()
    c = CircleFactory()
    client_code(s)
    client_code(c)