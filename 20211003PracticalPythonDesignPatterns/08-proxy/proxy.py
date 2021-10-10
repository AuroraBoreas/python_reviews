import time
from typing import Any, Callable, Union

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any)->Union[None,int]:
        key = (func.__name__, args)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args)
        return _cache[key]
    return memorized

class CalculatorProxy:
    def __init__(self, target:RawCalculator):
        self.target = target
        fib = getattr(self.target, 'fib')
        setattr(self.target, 'fib', memoir(fib))

    def __getattr__(self, attr):
        return getattr(self.target, attr)

if __name__ == '__main__':
    c = CalculatorProxy(RawCalculator())
    beg = time.time()
    fib_seq = [c.fib(x) for x in range(0, 80)]
    end = time.time()

    print(
        'Calculating the list of {} Fibonacci numbers took {} seconds'.format(
            len(fib_seq),
            end - beg
        )
    )

