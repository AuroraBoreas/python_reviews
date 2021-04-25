# python is a protocol orientated lang
# every top-level function has a corresponding dunder method

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print('time elapsed: ', end - start)
        return result
    return wrapper

def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('printer does stuff: ', result)
    return wrapper

def runner(n=2):
    def dec(func):
        def wrapper(*args, **kwargs):
            print('{.__name__}'.format(func))
            for _ in range(n):
                print(func(*args, **kwargs))
        return wrapper
    return dec

@runner(n=5)
@printer
@timer
def add(x, y):
    return x + y

@runner(n=3)
@printer
@timer
def sub(x, y):
    return x - y
