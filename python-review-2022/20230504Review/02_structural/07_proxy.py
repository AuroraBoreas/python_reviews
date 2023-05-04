"Python is a protocol orientated language; every top-level function implements its dunder method;" 

import functools
from typing import Any, Callable, ParamSpec, TypeVar


class Math:
    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)
    def fact(self, n: int, tail: int=1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail)

P = ParamSpec('P')
T = TypeVar('T')

def memoir(func: Callable[P, T]) -> Callable[P, T]:
    cache: dict = {}
    @functools.wraps(func)
    def memorized(*args: P.args, **kwargs: P.kwargs) -> T:
        key = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorized

class ProxyMath:
    def __init__(self, m: Math, attr: str) -> None:
        self._math = m
        func: Callable[P, T] = getattr(m, attr)
        setattr(self._math, attr, memoir(func))

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._math, attr)