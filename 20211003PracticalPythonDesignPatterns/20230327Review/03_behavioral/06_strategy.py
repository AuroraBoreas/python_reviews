# 

from typing import Any, Callable


class Executor:
    def __init__(self, func: Callable=None) -> None:
        if not func:
            raise ValueError
        self._func = func

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        return self._func(*args, **kwargs)
        