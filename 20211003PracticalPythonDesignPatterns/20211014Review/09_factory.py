from abc import ABCMeta

class Shape:
    def __init__(self): pass

class Square(Shape):
    def draw(self)->None:
        return 'Square drawed'

class Circle(Shape):
    def draw(self):
        return 'Circle drawed'
    
class AbstractFactory(metaclass=ABCMeta):
    def make_object(self): raise NotImplementedError()

class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square()

class CircleFactory(AbstractFactory):
    def make_object(self):
        return Circle()

if __name__ == '__main__':
    pass