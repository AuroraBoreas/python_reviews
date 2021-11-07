# avoid if...else...

from typing import Any, Callable

class Executionor:
    def __init__(self, func:Callable=None)->None:
        if not func:
            raise NotImplementedError()
        self.func = func

    def run(self,*args:Any,**kwargs:Any)->Any:
        return self.func(*args,**kwargs)

def addition(a:int, b:int)->int:
    return a + b

def subtraction(a:int, b:int)->int:
    return a - b

def multiple(a:int, b:int)->int:
    return a * b

def client_code()->None:
    e1 = Executionor(addition)
    e2 = Executionor(subtraction)
    e3 = Executionor(multiple)

    print(e1.run(1, 2))
    print(e2.run(1, 2))
    print(e3.run(1, 2))

if __name__ == '__main__':
    client_code()