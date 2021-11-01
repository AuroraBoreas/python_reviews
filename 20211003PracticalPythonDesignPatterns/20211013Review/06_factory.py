from abc import ABC, abstractmethod

### Inheritance 
class Shape:
    def __init__(self): pass

    def __str__(self): pass

    def draw(self): raise NotImplementedError()

    def move(self, direction:str): pass

    @classmethod
    def factory(cls, type:str):
        if type == 'circle': return
        if type == 'square': return
        assert 0, 'Bad Shape Request: ' + type

class Square(Shape): 
    def draw(self): pass

class Circle(Shape):
    def draw(self): pass

### Factory pattern
class AbstractFactory:
    __metaclass__ = ABC

    @abstractmethod
    def make_object(self): pass

class SquareFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Square()

class CircleFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Circle()

def draw_function(factory:AbstractFactory):
    drawable = factory.make_object()
    drawable.draw()

def prep_client():
    square_factory = SquareFactory()
    draw_function(square_factory)

    circle_factory = CircleFactory()
    draw_function(circle_factory)

if __name__ == '__main__':
    prep_client()