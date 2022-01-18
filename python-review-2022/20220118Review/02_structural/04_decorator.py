# 


from typing import Any, Callable
import functools, time, logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def timed(*args:Any, **kwargs:Any)->Any:
        b = time.perf_counter_ns()
        r = func(*args, **kwargs)
        e = time.perf_counter_ns()
        logging.info(f'time lapsed(ns) : {e-b:,.2f}')
        return r
    return timed


class RawMath:
    def __fib(self, n:int)->int: pass

    def __fact(self, n:int, rv:int=1)->int: pass

    @timer
    def fib(self, n:int)->int: return self.__fib(n)

    @timer
    def fact(self, n:int)->int: return self.__fact(n)