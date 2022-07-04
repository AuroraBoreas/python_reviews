"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Callable

class Executioner:
    def __init__(self, func:Callable=None) -> None:
        if not func:
            raise ValueError("func cannot be nullable")
        self._func = func

    def execute(self, *args:Any, **kwargs:Any) -> Any:
        return self._func(*args, **kwargs)

def add(a:int, b:int) -> int:
    return a + b

def mul(a:int, b:int) -> int:
    return a * b

def client_code() -> None:
    e = Executioner(add)
    rv = e.execute(3, 4)
    print(rv)

if __name__ == '__main__':
    client_code()
