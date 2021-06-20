"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import time
from typing import (List, TypeVar)
T = TypeVar('T', float, int, complex)

def compute(n:int)->List[T]:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == "__main__":
    for i in compute(10):
        print(i)