# 

from typing import Any, Callable, Dict


class MyMath:
    def fib(self, n:int)->int: pass
    def fact(self, n:int, rv:int=1)->int: pass

def memoir(func:Callable)->Callable:
    _cache:Dict = {}
    def memorized(*args:Any, **kwargs:Any)->Any:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

class ProxyMath:
    def __init__(self, target:MyMath, attr:str) -> None:
        self._target = target
        func = getattr(target, attr)
        setattr(self._target, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self._target, attr)