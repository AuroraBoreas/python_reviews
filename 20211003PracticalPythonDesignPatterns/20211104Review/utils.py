# utilties

import time
import functools
import logging
from typing import Any, Callable

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info(f'time lapsed(ns) : {end - beg}')
        return rv
    return inner