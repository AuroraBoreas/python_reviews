# strategy: get ride of if...else if..else

from typing import Any, Callable


class Executioner:
    def __init__(self, func:Callable=None)->None:
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
    add_ex = Executioner(add)
    mul_ex = Executioner(mul)
    print(add_ex.execute(4, 5))
    print(mul_ex.execute(4, 5))

if __name__ == '__main__':
    client_code()
