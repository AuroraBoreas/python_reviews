# 

import functools, time, logging
from typing import Any, Callable, Dict
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable) -> Callable:
    @functools.wraps(func)
    def inner(*args:Any, **kwargs:Any) -> Any:
        b = time.perf_counter()
        r = func(*args, **kwargs)
        e = time.perf_counter()
        logging.info(f'time lapsed(s) : {e - b:.5f}')
        return r
    return inner

class RawMath:
    def fib(self, n:int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)
    
    def fact(self, n:int, tail:int=1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail)

def memoir(func:Callable) -> Callable:
    _cache:Dict = dict()
    @functools.wraps(func)
    def inner(*args:Any, **kwargs:Any) -> Any:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return inner

class ProxyMath:
    def __init__(self, target:RawMath, attr:str) -> None:
        self._target = target
        func = getattr(target, attr)
        setattr(self._target, attr, memoir(func))

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._target, attr)

@timer
def client_code(attr:str, n:int=30) -> None:
    pm = ProxyMath(RawMath(), attr)
    f = getattr(pm, attr)
    r = f(n)
    print(r)

if __name__ == '__main__':
    client_code('fact', n=40)