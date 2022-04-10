"#" 

from typing import Any, Callable


class Executioner:
    def __init__(self, func:Callable) -> None:
        if not func:
            raise NotImplementedError()
        self._func = func

    def execute(self, *args:Any, **kwargs:Any)->Any:
        return self._func(*args, **kwargs)

def fact(n:int, res:int=1)->int:
    return res if n < 2 else fact(n - 1, n * res)