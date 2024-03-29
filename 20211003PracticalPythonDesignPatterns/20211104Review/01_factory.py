# factory

from abc import ABCMeta, abstractmethod

class Shape:
    def __init__(self):pass

    def draw(self): pass


class Square(Shape):
    def __init__(self): pass

    def draw(self)->None: print(f'{self.__class__} starts drawing..') 

class Circle(Shape):
    def __init__(self): pass

    def draw(self)->None: print(f'{self.__class__} starts drawing..') 


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_object(self)->Shape: pass

class CircleFactory(Factory):
    def make_object(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> Shape:
        return Square()

def client_code(f:Factory)->None:
    drawable = f.make_object()
    drawable.draw()

if __name__ == '__main__':
    s = SquareFactory()
    c = CircleFactory()
    client_code(s)
    client_code(c)
