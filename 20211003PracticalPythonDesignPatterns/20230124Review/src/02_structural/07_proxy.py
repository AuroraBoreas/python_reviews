
from ast import Tuple
import functools
from typing import Any, Callable


class MyMath:
    def fib(self, n: int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)
    def fact(self, n: int, tail: int=1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail)

def memoir(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    cache: dict[Tuple, Any] = {}
    @functools.wraps(func)
    def memorized(*args: Any, **kwargs: Any) -> Any:
        key: Tuple = (func.__name__, args.__hash__, kwargs.__hash__)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorized

class ProxyMath:
    def __init__(self, mm: MyMath, attr: str) -> None:
        self._mm = mm
        func: Callable = getattr(mm, attr)
        setattr(self._mm, attr, memoir(func))

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._mm, attr)
