# proxy

from typing import Any, Callable

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int)->int:
        return 1 if n < 2 else self.fact(n-1) * n


def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any, **kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

class ProxyCalculator:
    def __init__(self, target:RawCalculator, attr:str)->None:
        self.target = target
        func = getattr(self.target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)

import time
def client_code(attr:str, ub:int=80)->None:
    beg = time.perf_counter_ns()
    p = ProxyCalculator(RawCalculator(), attr)
    f = getattr(p, attr)
    seq = [f(x) for x in range(ub)]
    end = time.perf_counter_ns()
    print('time lapsed(ns): {}'.format(end - beg))
    print(seq)

if __name__ == '__main__':
    for attr in ['fib', 'fact']:
        client_code(attr)