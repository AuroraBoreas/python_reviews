"#Python is a protocol orientated lang; every top-level function has corresponding dunder method implemented;" 

def fibonacci(n: int)->int:
    """my fibonacci

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n: int)->int:
    """my factorial

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return 1 if n < 2 else n * fibonacci(n-1)

from dis import dis
import functools
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def display(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        logging.debug(rv)
    return wrapper


@display
def myfib(n: int)->int:
    """myfib

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return fibonacci(n)

@display
def myfact(n: int)->int:
    """myfact

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return factorial(n)

if __name__ == '__main__':
    myfib(5)
    myfact(5)