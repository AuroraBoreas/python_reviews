"#Python is a protocol orientated lang;every top-level function has a corresponding dunder method implemented;" 

import time
from typing import TypeVar
T = TypeVar('T', int, float, complex)

class Compute:
    def __init__(self, last:T):
        self.last  = last
        self.first = 0

    def __iter__(self):
        return self

    def __next__(self):
        rv = self.first
        self.first += 1
        time.sleep(.5)
        if self.first > self.last:
            raise StopIteration()
        return rv

if __name__ == "__main__":
    for i in Compute(10):
        print(i)