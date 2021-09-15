"Python is a protocol orientated lang; every top-level function has a corresponding dunder method;" 

import time
from typing import TypeVar
T = TypeVar('T', int, float, complex)

def compute(n:int)->List[T]:
    rv = []
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == '__main__':
    for i in compute(10):
        print(i)