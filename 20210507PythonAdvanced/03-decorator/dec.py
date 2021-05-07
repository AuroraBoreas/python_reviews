"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import functools

def display(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print(rv)
    return wrapper


@display
def myfib(n: int)->None:
    return fibonacci(n)

@display
def myfact(n: int)->None:
    return factorial(n)

if __name__ == '__main__':
    myfib(5)
    myfact(5)