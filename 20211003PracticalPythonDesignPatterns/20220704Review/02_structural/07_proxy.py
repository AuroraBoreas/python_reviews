"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Callable, Dict
import time

class Math:
    def fib(self, n:int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)

    def fact(self, n:int) -> int:
        return 1 if n < 2 else n * self.fact(n - 1)

def memoir(func:Callable) -> Callable:
    _cache:Dict = {}
    def memorized(*args:Any, **kwargs:Any) -> Any:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

class ProxyMath:
    def __init__(self, target:Math, attr:str) -> None:
        self._target = target
        func = getattr(target, attr)
        setattr(self._target, attr, memoir(func))

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._target, attr)

def client_code() -> None:
    c = ProxyMath(Math(), 'fib')
    beg = time.time()
    fib_seq = [c.fib(x) for x in range(0, 100)]
    end = time.time()

    print(
        'Calculating the list of {} Fibonacci numbers took {} seconds'.format(
            len(fib_seq),
            end - beg
        )
    )

if __name__ == '__main__':
    client_code()