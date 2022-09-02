"#" 

from typing import Any, Callable


class Executor:
    def __init__(self, func:Callable=None) -> None:
        if not func:
            raise ValueError()
        self._func = func

    def execute(self, *args:Any, **kwargs:Any) -> Any:
        return self._func(*args, **kwargs)

def add(a:int, b:int) -> int:
    return a + b

def sub(a:int, b:int) -> int:
    return a - b

def client_code() -> None:
    e = Executor(add)
    print(e.execute(3, 4))
    e._func = sub
    print(e.execute(3, 4))

if __name__ == '__main__':
    client_code()