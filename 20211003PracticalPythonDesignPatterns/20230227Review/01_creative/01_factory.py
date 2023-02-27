# 

from abc import ABC, abstractmethod


class Shape:
    def draw(self) -> str:
        raise NotImplementedError

class Circle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing.."

class Rectangle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing.."
    
class Factory(ABC):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError
    
class CircleFactory(Factory):
    def drawable(self) -> Shape:
        return Circle()
    
class RectangleFactory(Factory):
    def drawable(self) -> Shape:
        return Rectangle()

def client_code(f: Factory) -> None:
    d: Shape = f.drawable()
    print(d.draw())

def main() -> None:
    for f in [
        CircleFactory(),
        RectangleFactory(),
    ]:
        client_code(f)

if __name__ == '__main__':
    main()