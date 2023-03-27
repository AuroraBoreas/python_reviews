# 

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self) -> None:
        raise NotImplementedError
    
class Circle(Shape):
    def draw(self) -> None:
        return f'{self.__class__} starts drawing..'
    
class Rectangle(Shape):
    def draw(self) -> None:
        return f'{self.__class__} starts drawing..'
    
class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError
    
class CircleFactory(IFactory):
    def drawable(self) -> Shape:
        return Circle()
    
class RectangleFactory(IFactory):
    def drawable(self) -> Shape:
        return Rectangle()

def client_code(f: IFactory) -> None:
    d = f.drawable()
    print(d.draw())

def main() -> None:
    for factory in [
        CircleFactory(),
        RectangleFactory()
    ]:
        client_code(factory)

if __name__ == '__main__':
    main()