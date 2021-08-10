"Python is a protocol orientated language, every top-level function has a corresponding dunder method" 

import time

def compute(n:int)->list:
    rv = []
    for i in range(n):
        rv.append(i)
        time.sleep(.5)

if __name__ == '__main__':
    for i in compute(10):
        print(i)