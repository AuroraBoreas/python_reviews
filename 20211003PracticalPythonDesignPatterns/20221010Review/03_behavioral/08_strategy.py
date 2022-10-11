#

from typing import Any, Callable


class Executioner:
    def __init__(self, func:Callable=None) -> None:
        if not func:
            raise ValueError
        self.func = func
    
    def execute(self, *args:Any, **kwargs:Any) -> Any:
        return self.func(*args, **kwargs)

def fib(n:int) -> int:
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)

def fact(n:int) -> int:
    return 1 if n < 2 else n * fact(n - 2)

def gcd(a:int, b:int) -> int:
    return a if b == 0 else gcd(b, a%b)

def client_code() -> None:
    for func in [fib, fact]:
        e = Executioner(func)
        res = e.execute(10)
        print(res)

if __name__ == '__main__':
    client_code()
