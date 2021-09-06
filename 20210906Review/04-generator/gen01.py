"Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

import time
from typing import TypeVar, List
T = TypeVar('T', int, float, complex)

def compute(n:int)->List[T]:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == '__main__':
    for i in compute(10):
        print(i)