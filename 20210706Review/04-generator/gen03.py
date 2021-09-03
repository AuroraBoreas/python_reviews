"#python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import time
from typing import TypeVar
T = TypeVar('T', int, float, complex)

def compute(n:int)->int:
    rv = []
    for i in range(n):
        yield i
        time.sleep(.5)

if __name__ == "__main__":
    for i in compute(10):
        print(i)