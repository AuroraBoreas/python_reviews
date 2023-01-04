"#" 

import functools
from typing import Callable, ParamSpec, TypeVar, Any
P = ParamSpec('P')
T = TypeVar('T')

class RawMath:
    def fib(self, n: int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)

    def fact(self, n: int, tail: int=1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail)

def memoir(func: Callable[P, T]) -> Callable[P, T]:
    _cache: dict = {}
    @functools.wraps(func)
    def memorized(*args: P.args, **kwargs: P.kwargs) -> T:
        key: tuple = (func.__hash__, args.__hash__, kwargs.__hash__)
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

class MyMath:
    def __init__(self, rm: RawMath, attr: str) -> None:
        self._rm: RawMath = rm
        func: Callable[P, T] = getattr(rm, attr)
        setattr(self._rm, attr, memoir(func))
    
    def __getattr__(self, attr: str) -> Any:
        return getattr(self._rm, attr)