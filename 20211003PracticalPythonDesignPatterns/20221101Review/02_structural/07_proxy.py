"#" 

import functools
from typing import Any, Callable, Dict


def memoir(func:Callable) -> Callable:
    cache:Dict = {}
    @functools.wraps(func)
    def memorized(*args:Any, **kwargs:Any) -> Any:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorized

class RawMath:
    def fib(self, n:int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)
    def fact(self, n:int) -> int:
        return 1 if n < 2 else n * self.fact(n - 1)

class MyMath:
    def __init__(self, rawMath:RawMath, attr:str) -> None:
        self._rawMath = rawMath
        func = getattr(rawMath, attr)
        setattr(self._rawMath, attr, memoir(func))

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._rawMath, attr)

def client_code() -> None:
    mm:MyMath = MyMath(RawMath(), 'fib')
    print(mm.fib(300))

if __name__ == '__main__':
    client_code()