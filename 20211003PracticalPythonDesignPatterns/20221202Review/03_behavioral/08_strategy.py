"#" 

from typing import Any, Callable


class Strategy:
    def __init__(self, func:Callable=None) -> None:
        if not func:
            raise ValueError("func is None")
        self.func = func
    
    def execute(self, *args:Any, **kwargs:Any) -> Any:
        return self.func(*args, **kwargs)