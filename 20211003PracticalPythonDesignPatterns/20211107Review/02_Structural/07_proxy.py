# proxy

class RawMath:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int)->int:
        return 1 if n < 2 else self.fact(n-1) * n

from typing import Callable, Any

def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class ProxyMath:
    def __init__(self, target:RawMath, attr:str)->None:
        self.target = target
        func = getattr(target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)
