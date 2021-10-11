#Python is a protocol orientated lang; every top-level function has a correspoding dunder method implemented; 

from typing import List
import time

def compute(n:int)->List[int]:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == '__main__':
    for i in compute(10):
        print(i)