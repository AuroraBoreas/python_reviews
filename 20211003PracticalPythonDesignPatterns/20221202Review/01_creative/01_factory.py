"#" 

from abc import ABCMeta, abstractmethod


class Shape:
    def draw(self) -> str:
        raise NotImplementedError()

class Circle(Shape):
    def draw(self) -> str:
        return f'{self.__class__} start drawing...'

class Square(Shape):
    def draw(self) -> str:
        return f'{self.__class__} start drawing...'

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def drawable(self) -> Shape:
        raise NotImplementedError()

class CircleFactory(Factory):
    def drawable(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def drawable(self) -> Shape:
        return Square()

def client_code(f:Factory) -> None:
    d:Shape = f.drawable()
    print(d.draw())

def main() -> None:
    for f in [
        CircleFactory(),
        SquareFactory()
    ]:
        client_code(f)

if __name__ == '__main__':
    main()