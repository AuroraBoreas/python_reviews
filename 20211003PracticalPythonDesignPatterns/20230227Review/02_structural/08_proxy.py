# 

import functools
from typing import Any, Callable, ParamSpec, TypeVar
P = ParamSpec('P')
T = TypeVar('T')

class Math:
    def fib(self, n: int) -> int:
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)
    
    def fact(self, n: int, tail: int = 1) -> int:
        return tail if n < 2 else self.fact(n - 1, n * tail) 

    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a%b)
    
def memoir(func: Callable[P, T]) -> Callable[P, T]:
    cache: dict = dict()
    @functools.wraps(func)
    def memorize(*args: tuple[Any], **kwargs: dict[Any]) -> Any:
        key: tuple = func.__name__, args.__hash__, kwargs.__hash__
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorize

class ProxyMath:
    def __init__(self, math: Math, attr: str) -> None:
        self._math = math
        func = getattr(math, attr)
        setattr(self._math, attr, memoir(func))
    
    def __getattr__(self, attr: str) -> Any:
        return getattr(self._math, attr)
    
def client_code() -> None:
    math: Math = Math()
    for attr in [
        # 'gcd',
        'fib',
        'fact',
    ]:
        pm: ProxyMath = ProxyMath(math, attr)
        print(pm.__getattr__(attr)(10))

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()