# 

import functools
from typing import Any, Callable, ParamSpec, TypeVar


class Math:
    def fib(self, n: int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)

    def fact(self, n: int, tail: int=1) -> int:
        return tail if n < 2 else self.fact(n - 1, tail * n)


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
        self._m = m
        func = getattr(m, attr)
        setattr(self._m, attr, memoir(func))

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._m, attr)