# fence

from typing import Any, Callable
import functools

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2) 

    def fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.fact(n-1, n * rv)

def memoir(func:Callable)->Callable:
    _cache = {}
    @functools.wraps(func)
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
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

def client_code(attr:str, n:int)->None:
    p = ProxyCalculator(RawCalculator(), attr)
    f = getattr(p, attr)
    rv = [f(x) for x in range(n)]
    print(f'{attr} sequencing, length={n} : ')
    print(rv)

if __name__ == '__main__':
    n:int = 20
    for attr in ['fib', 'fact']:
        client_code(attr, n)