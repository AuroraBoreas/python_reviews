# factory

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self) -> None: pass

class Circle(Shape):
    def draw(self) -> None:
        print('drawing circle..')

class Square(Shape):
    def draw(self) -> None:
        print('drawing square..')

class Factory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_object(self) -> Shape: pass

class CircleFactory(Factory):
    def make_object(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> Shape:
        return Square()

def client_code(factory:Factory) -> None:
    drawable = factory.make_object()
    drawable.draw()

if __name__ == '__main__':
    c = CircleFactory()
    s = SquareFactory()
    client_code(c)
    client_code(s)