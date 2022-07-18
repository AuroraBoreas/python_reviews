"#" 

import functools
from typing import Any, Callable


class RawMath:
    def fib(self, n:int) -> int: pass
    def fact(self, n:int) -> int: pass

def memoir(func:Callable) -> Callable:
    _cache = {}
    @functools.wraps(func)
    def inner(*args:Any, **kwargs:Any) -> Any:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return inner

class ProxyMath:
    def __init__(self, rm:RawMath, attr:str) -> None:
        self._rm = rm
        func = getattr(rm, attr)
        setattr(self._rm, memoir(func))

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._rm, attr)