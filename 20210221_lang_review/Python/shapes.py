"""

a simple module demonstrates "interface" concept in Python

@ZL, 202103

"""

import typing, math
Any = typing.Any

class IShape:
    def circumference(self):
        pass

    def area(self):
        pass

class Circle(IShape):
    def __init__(self, radius: Any):
        self._radius = float(radius)

    def circumference(self):
        return math.pi * self._radius * 2
        
    def area(self):
        return math.pi * math.pow(self._radius, 2)

class Rectangle(IShape):
    def __init__(self, length: Any, width: Any):
        self._length = float(length)
        self._width = float(width)
        
    def circumference(self):
        return (self._length + self._width) * 2
        
    def area(self):
        return self._length * self._width

class Triangle(IShape):
    def __init__(self, base: Any, height: Any):
        self._base = float(base)
        self._height = float(height)
        
    def circumference(self):
        hyp: float = math.pow(math.pow(self._base, 2) + math.pow(self._height, 2), 0.5)
        return self._base + self._height + hyp
        
    def area(self):
        return self._base * self._height / 2