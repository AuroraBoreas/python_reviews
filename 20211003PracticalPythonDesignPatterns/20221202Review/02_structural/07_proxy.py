"#" 

from typing import Any, Callable, Dict


def memoir(func:Callable) -> Callable:
    cache:Dict = {}
    def memorized(*args:Any, **kwargs:Any) -> Any:
        key = (func, args.__hash__, kwargs.__hash__)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorized

class RawMath:
    def fib(self, n:int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)
    
    def fact(self, n:int, tail:int=1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail)

class MyMath:
    def __init__(self, rm:RawMath, attr:str) -> None:
        self._rm = rm
        func = getattr(rm, attr)
        setattr(self._rm, attr, memoir(func))
    
    def __getattr__(self, attr:str) -> Any:
        return getattr(self._rm, attr)

def client_code() -> None:
    mm = MyMath(RawMath(), 'fib')
    res = mm.fib(100)
    print(res)

if __name__ == '__main__':
    client_code()

