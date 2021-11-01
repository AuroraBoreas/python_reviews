
import time
import functools
from typing import Callable, Any, Dict

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Dict[Any,Any])->Any:
        beg = time.time()
        rv  = func(*args, **kwargs)
        end = time.time()
        print('time lapsed(s) : {0:.5f}'.format(end - beg))
        return rv
    return inner

@timer
class MyMath:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int, rv=1)->int:
        return rv if n < 2 else self.fact(n-1, n*rv)

if __name__ == '__main__':
    mm = MyMath()
    rv1 = mm.fib(5)
    print(rv1)
    rv2 = mm.fact(5)
    print(rv2)