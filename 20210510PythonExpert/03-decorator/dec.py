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
        rv = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print("time lapsed: {0}".format(end - start))
        return rv
    return wrapper

@timer
def myfib(n: int)->int:
    """my fibonacci formula

    :param n: [description]
    :type n: int
    :return: [description]
    :rtype: int
    """
    return fibonacci(n)

@timer
def myfact(n: int)->int:
    """my factorial formula

    :param n: [description]
    :type n: int
    :return: [description]
    :rtype: int
    """
    return factorial(n)

if __name__ == '__main__':
    myfact(5)
    myfib(5)
