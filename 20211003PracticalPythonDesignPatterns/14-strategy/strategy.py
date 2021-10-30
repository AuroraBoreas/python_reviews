# strategy

from typing import Callable, Any

class StrategyExecutor:
    def __init__(self, strategy:Callable=None)->None:
        self.strategy = strategy

    def execute(self, *args:Any, **kwargs:Any)->Any:
        if not self.strategy:
            return 'NotImplementedError'
        return self.strategy(*args,**kwargs)

def addition(arg1:int, arg2:int)->int:
    return arg1 + arg2

def subtraction(arg1:int, arg2:int)->int:
    return arg1 - arg2

def client_code():
    se = StrategyExecutor()
    addition_strategy = StrategyExecutor(addition)
    subtraction_strategy = StrategyExecutor(subtraction)
    print(addition_strategy.execute(4, 6))
    print(subtraction_strategy.execute(4, 6))
    print(se.execute(4, 6))

if __name__ == '__main__':
    client_code()