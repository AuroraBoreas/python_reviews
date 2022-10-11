# 

import functools
from typing import Any, Callable, Dict, Tuple


class RawMath:
    def fib(self, n:int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)
    def fact(self, n:int) -> int:
        return 1 if n < 2 else n * self.fact(n - 1) 

def memoir(func:Callable) -> Callable:
    _cache:Dict = {}
    @functools.wraps(func)
    def memorized(*args:Any, **kwargs:Any) -> Any:
        key:Tuple = (func.__name__, args.__hash__, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

class MyMath:
    def __init__(self, rm:RawMath, attr:str) -> None:
        self._rm = rm
        func = getattr(rm, attr)
        setattr(self._rm, attr, memoir(func))

    def getattr(self, attr:str) -> Any:
        return getattr(self._rm, attr)