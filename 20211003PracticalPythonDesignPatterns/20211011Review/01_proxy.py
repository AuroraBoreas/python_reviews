from __future__ import annotations
from typing import Any, Callable, Dict
import functools

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

def memoir(func:Callable[...,Any])->Callable[...,Any]:
    _cache = {}
    @functools.wraps(func)
    def memorized(*args:Any,**kwargs:Dict[Any,Any])->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class ProxyCalculator:
    def __init__(self, target:RawCalculator):
        self.target = target
        fib = getattr(self.target, 'fib')
        setattr(self.target, 'fib', memoir(fib))

    def __getattr__(self, attr):
        return getattr(self.target, attr)

if __name__ == '__main__':
    import time
    p = ProxyCalculator(RawCalculator())
    beg = time.perf_counter()
    fib_seq = [p.fib(x) for x in range(0, 80)]
    end = time.perf_counter()
    print(
        '{} Fibonacci numbers take {} seconds'.format(
            len(fib_seq),
            end - beg
        )
    )

    print(fib_seq)
