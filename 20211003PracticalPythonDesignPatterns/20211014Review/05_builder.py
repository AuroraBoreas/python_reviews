from __future__ import annotations

class Shape:
    def __init__(self): pass

    def __str__(self)->str: return 'Shape: {0!r}'.format(self)

    def draw(self): pass

    @staticmethod
    def factory(stype:str)->Shape:
        if stype == 'Circle':
            return Circle()
        elif stype == 'Square':
            return Square()
        else:
            assert 0, 'Bad Shape Request: ' + stype

class Circle(Shape):
    def draw(self)->str:
        return 'Shape: Circle'

class Square(Shape):
    def draw(self)->str:
        return 'Shape: Square'


if __name__ == '__main__':
    s = Shape()
    print(s.factory('Circle'))