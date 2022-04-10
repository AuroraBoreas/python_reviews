"#" 

import functools
from typing import Any, Callable


class MyMath:
    def fib(self, n:int)->int: pass
    def fact(self, n:int)->int: pass

def memoir(func:Callable)->Callable:
    cache = {}
    @functools.wraps(func)
    def memorized(*args:Any, **kwargs:Any)->Any:
        key = (func.__name__, func.__hash__)
        if not key in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorized

class ProxyMath:
    def __init__(self, m:MyMath, attr:str) -> None:
        self._m = m
        func = getattr(m, attr)
        setattr(self._m, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self._m, attr)