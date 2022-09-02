"#" 

from typing import Any, Callable, Dict


class RawMath:
    def fib(self, n:int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)

    def fact(self, n:int, tail:int = 1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail)

def memorize(func:Callable) -> Callable:
    _cache:Dict = {}
    def memoir(*args:Any, **kwargs:Any) -> Any:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memoir

class ProxyMath:
    def __init__(self, rm:RawMath, attr:str) -> None:
        self._rm = rm
        func = getattr(rm, attr)
        setattr(self._rm, attr, memorize(func))

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._rm, attr)