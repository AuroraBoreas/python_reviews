"#python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented"  

import time

def compute(n: int)->list:
    rv = list()
    for i in range(n):
        time.sleep(.5)
        rv.append(i)
    return rv

if __name__ == '__main__':
    print(compute(10))