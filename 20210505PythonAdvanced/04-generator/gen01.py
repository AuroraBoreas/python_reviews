"#Python is a protocl orientated lang; every top-level function has a corresponding dunder method implemented;" 

import time

def compute(n:int)->list:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv


if __name__ == '__main__':
    print(compute(10))