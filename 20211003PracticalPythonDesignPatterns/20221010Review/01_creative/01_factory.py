# 

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self) -> None:
        raise NotImplementedError()
        
class Circle(Shape):
    def draw(self) -> None:
        print(f'{self.__class__} starts drawing..')

class Rectangle(Shape):
    def draw(self) -> None:
        print(f'{self.__class__} starts drawing..')

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError()

class CircleFactory(Factory):
    def drawable(self) -> Shape:
        return Circle()

class RectangleFactory(Factory):
    def drawable(self) -> Shape:
        return Rectangle()

def client_code(f:Factory) -> None:
    d = f.drawable()
    d.draw()

def main() -> None:
    for i in [
        CircleFactory(),
        RectangleFactory(),
    ]:
        client_code(i)

if __name__ == '__main__':
    main()