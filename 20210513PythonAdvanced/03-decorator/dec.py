"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        rv    = func(*args, **kwargs)
        end   = time.perf_counter_ns()
        print('time lapsed(ns): {0}'.format(end - start))
        return rv
    return wrapper

@timer
def myfib(n: int)->int:
    return fibonacci(n)

@timer
def myfact(n: int)->int:
    return factorial(n)

if __name__ == "__main__":
    rv1 = myfib(5)
    # print(rv1)
    rv2 = myfact(5)
    # print(rv2)