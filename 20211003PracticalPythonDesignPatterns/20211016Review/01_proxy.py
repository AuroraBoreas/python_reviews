
from typing import (Callable, Dict, Any)

def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any,**kwargs:Dict[Any,Any])->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int)->int:
        return 1 if n < 2 else n * self.fact(n-1)
    
class ProxyCalculator:
    def __init__(self, target:RawCalculator, attr:str)->None:
        self.target = target
        func = getattr(target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)

if __name__ == '__main__':
    import time

    beg = time.time()
    p = ProxyCalculator(RawCalculator(), 'fib')
    fib_seq = [p.fib(x) for x in range(80)]
    print(fib_seq)

    p2 = ProxyCalculator(RawCalculator(), 'fact')
    fact_seq = [p.fact(x) for x in range(80)]
    print(fact_seq)
    end = time.time()

    print('takes {} seconds'.format(end - beg))