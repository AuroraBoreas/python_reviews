"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from abc import ABCMeta, abstractmethod

class Shape:
    def draw(self) -> str:
        raise NotImplementedError
    
class Circle(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing..."
    
class Square(Shape):
    def draw(self) -> str:
        return f"{self.__class__} starts drawing..."
    
class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError

class CircleFactory(IFactory):
    def drawable(self) -> Shape:
        return Circle()

class SquareFactory(IFactory):
    def drawable(self) -> Shape:
        return Square()
    
def client_code(f: IFactory) -> None:
    drawable: Shape = f.drawable()
    print(drawable.draw())

def main() -> None:
    for f in [
        CircleFactory(),
        SquareFactory(),
    ]:
        client_code(f)

if __name__ == '__main__':
    main()