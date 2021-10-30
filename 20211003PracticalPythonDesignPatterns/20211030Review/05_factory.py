# str -> object

from abc import ABC, abstractmethod


class Shape:
    def __init__(self): pass

    def draw(self)->None: pass

class Circle(Shape):
    def draw(self) -> None:
        print(f'{self.__class__} drawing..')

class Square(Shape):
    def draw(self) -> None:
        print(f'{self.__class__} drawing..')

class Factory(ABC):
    @abstractmethod
    def make_object(self): pass

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
    c = CircleFactory()
    s = SquareFactory()
    client_code(c)
    client_code(s)