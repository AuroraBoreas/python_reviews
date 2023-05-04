"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec('P')
T = TypeVar('T')

class Executor:
    def __init__(self, func: Callable[P, T]=None) -> None:
        if not func:
            raise ValueError
        self.func = func

    def execute(self, *args: P.args, **kwargs: P.kwargs) -> Any:
        return self.func(*args, **kwargs)