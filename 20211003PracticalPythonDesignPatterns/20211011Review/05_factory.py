from abc import abstractmethod, ABC
class Shape:
    def __init__(self): pass
    def __str__(self): return

    @staticmethod
    def draw(type:str)->object:
        if type == 'Square':
            return Square()
        elif type == 'Circle':
            return Circle()
        else:
            assert 0, 'Bad Shape request: ' + type

class Square:
    def __init__(self):
        pass
    def __str__(self): return
    def draw(self)->None:
        print('drawing a square..')

class Circle:
    def __init__(self):
        pass
    def __str__(self): return
    def draw(self)->None:
        print('draw a circle..')

class Factory(ABC):
    @abstractmethod
    def make_object(self)->object:
        raise NotImplementedError()

class CircleFactory(Factory):
    def make_object(self) -> object:
        return Circle()

class SquareFactory(Factory):
    def make_object(self) -> object:
        return Square()

def draw(factory:Factory)->None:
    drawable = factory.make_object()
    drawable.draw()

def client_code()->None:
    s = SquareFactory()
    draw(s)
    c = CircleFactory()
    draw(c)

if __name__ == '__main__':
    client_code()
