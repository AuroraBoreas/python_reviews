"# python is a protocol orientated lang;\n# every top-level function has a corresponding dunder method implemented;" 


"""

context

[ wrapper ]
===
* what?
A: passing a function into another function do some extra stuff inside return result;

* why?
A: make life easier

* how to?
A: wrapper

===

@ZL, 20210426

"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        rv = func(*args, **kwargs)
        end   = time.perf_counter()
        print('{.__name__} time elapsed: {}'.format(func, end-start))
        return rv
    return wrapper

@timer
def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

@timer
def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    print(fibonacci(5))
    print(factorial(5))
    