# proxy

from typing import Callable, Any


class RawCalculator:
    def fact(self, n:int)->int:
        return 1 if n < 2 else n * self.fact(n-1)

    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)


def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class ProxyCalculator:
    def __init__(self, target:RawCalculator, attr:str)->None:
        self.target = target
        func = getattr(self.target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)
