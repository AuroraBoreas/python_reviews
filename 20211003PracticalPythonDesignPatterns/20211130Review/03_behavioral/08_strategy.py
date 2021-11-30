# 

from typing import Any, Callable


class Executioner:
    def __init__(self, func:Callable=None) -> None:
        if not func:
            raise NotImplementedError()
        self._func = func
    
    def execute(self, *args:Any, **kwargs:Any)->Any:
        return self._func(*args, **kwargs)