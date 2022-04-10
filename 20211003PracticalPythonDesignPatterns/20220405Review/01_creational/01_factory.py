"factory: give a string => return an object;" 

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self)->str:
        raise NotImplementedError()

class Rectangle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing.."

class Circle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing.."

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def drawable(self)->Shape:
        raise NotImplementedError()

class RectangleFactory(Factory):
    def drawable(self) -> Shape:
        return Rectangle()

class CircleFactory(Factory):
    def drawable(self) -> Shape:
        return Circle()

def client_code(factory:Factory)->None:
    o = factory.drawable()
    print(o.draw())

if __name__ == '__main__':
    factories = [
        RectangleFactory(),
        CircleFactory(),
    ]

    for factory in factories:
        client_code(factory)