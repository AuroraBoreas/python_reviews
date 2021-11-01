# return object based on a given str

from abc import ABCMeta, abstractmethod

class Shape:
    def __init__(self): pass
    @abstractmethod
    def draw(self): pass

class Circle(Shape):
    def draw(self)->None:
        print('drawing a circle...')

class Square(Shape):
    def draw(self)->None:
        print('drawing a square...')

class Factory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self)->None: raise NotImplementedError()

class CircleFactory(Factory):
    def draw(self)->None:
        return Circle()

class SquareFactory(Factory):
    def draw(self)->None:
        return Square()

def client_code(factory:Factory):
    drawable = factory.draw()
    drawable.draw()

if __name__ == '__main__':
    c = CircleFactory()
    s = SquareFactory()
    client_code(c)
    client_code(s)
