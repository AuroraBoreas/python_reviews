#Python is a protocol orientated lang; every top-level function has a correspoding dunder method implemented; 

from typing import List
import time

def compute(n:int)->int:
    rv = list()
    for i in range(n):
        yield i
        time.sleep(.5)

if __name__ == '__main__':
    for i in compute(10):
        print(i)