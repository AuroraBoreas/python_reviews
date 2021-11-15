# proxy
import time
from typing import Any, Callable


class MyMath:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.fact(n-1, n*rv) 


def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

class ProxyMath:
    def __init__(self, target:MyMath, attr:str) -> None:
        self.target = target
        func = getattr(self.target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)

def client_code(attr:str, n:int=30)->None:
    b = time.perf_counter_ns()
    p = ProxyMath(MyMath(), attr)
    f = getattr(p, attr)
    s = [f(x) for x in range(n)]
    e = time.perf_counter_ns()
    print(f'\ntime lapsed(ns) : {e-b:,.2f}')
    print(s)