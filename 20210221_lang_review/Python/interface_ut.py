"""

a simple unittest validates if "interface" works

@ZL, 202103

"""

from shapes import (IShape, Circle, Rectangle, Triangle)

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def main():
    shapes: list = [
        Circle(5),
        Rectangle(3, 3),
        Rectangle(4, 4),
        Triangle(3, 4),
    ]

    for shape in shapes:
        logging.debug("type: {0}, circumference = {1:.2f}, area = {2:.2f}"
                      .format(type(shape),
                              shape.circumference(), 
                              shape.area()))


if __name__ == '__main__':
    main()