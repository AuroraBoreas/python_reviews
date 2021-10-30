
from abc import ABC, abstractmethod

class Shape:
    def __init__(self)->None:
        pass
    def draw(self): pass

class Circle(Shape):
    def draw(self):
        return 'drawing circle'

class Square(Shape):
    def draw(self):
        return 'drawing square'

class AbstractFactory(ABC):
    @abstractmethod
    def make_object(self)->Shape: pass

class CircleFactory(AbstractFactory):
    def make_object(self)->Circle:
        return Circle()

class SquareFactory(AbstractFactory):
    def make_object(self)->Square:
        return Square()

def client_code(factory:AbstractFactory)->None:
    drawable = factory.make_object()
    drawable.draw()