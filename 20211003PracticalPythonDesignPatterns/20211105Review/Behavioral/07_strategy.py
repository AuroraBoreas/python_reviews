# no more fuckin if else

from typing import Any, Callable, TypeVar
T = TypeVar('T', int, float, complex)

class Executor:
    def __init__(self, strategy:Callable=None)->None:
        self.strategy = strategy

    def execute(self, *args:Any, **kwargs:Any)->Any:
        return self.strategy(*args,**kwargs)

def addition(a:T, b:T)->T:
    return a + b

def subtraction(a:T, b:T)->T:
    return a - b

def multiple(a:T, b:T)->T:
    return a * b

def client_code()->None:
    add = Executor(addition)
    sub = Executor(subtraction)
    mul = Executor(multiple)
    print(add.execute(4, 5))
    print(sub.execute(4, 5))
    print(mul.execute(4, 5))

if __name__ == '__main__':
    client_code()
