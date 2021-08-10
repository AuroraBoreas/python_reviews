"Python is a protocol orientated language, every top-level function has a corresponding dunder method" 

import time

def compute(n:int)->int:
    for i in range(n):
        yield i
        time.sleep(.5)

if __name__ == '__main__':
    for i in compute(10):
        print(i)