"#" 

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

from typing import ParamSpec, TypeVar, Callable
P = ParamSpec('P')
T = TypeVar('T')

class Executor:
    def __init__(self, fn: Callable[P, T] = None) -> None:
        if not fn:
            raise ValueError('fn is None')
        self._fn: Callable[P, T] = fn

    def execute(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self._fn(*args, **kwargs)

def add(a: int | float, b: int | float) -> int | float:
    return a + b

def sub(a: int | float, b: int | float) -> int | float:
    return a - b

def client_code() -> None:
    e: Executor = Executor(add)
    logging.info(e.execute(2, 3))
    e._fn = sub
    logging.info(e.execute(2.3, 1.0))

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()
