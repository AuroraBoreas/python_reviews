# strategy avoid redundant if...else if...else

from typing import Any, Callable


class Executioner:
    def __init__(self, func:Callable=None) -> None:
        if func is None:
            raise NotImplementedError()
        self.func = func
    
    def execute(self, *args:Any, **kwargs:Any)->Any:
        return self.func(*args, **kwargs)

def add(a:int, b:int)->int:
    return a + b

def mul(a:int, b:int)->int:
    return a * b

def client_code()->None:
    ea = Executioner(add)
    eb = Executioner(mul)

    ea.execute(4, 5)
    eb.execute(4, 5)