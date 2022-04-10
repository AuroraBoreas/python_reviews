"python is a protocol orientated lang; every high level function has a corresponding dunder method implemented;" 

from typing import Any, Callable, Dict, Type


class Base:
    def foo(self)->str:
        return self.bar()

old_bc = __build_class__

def my_bc(func:Callable, name:Type, base:Dict=None)->Any:
    if base:
        if Base is base:
            assert 'bar' in func.__code__.co_names, f'bar not found in class {name}'
            return old_bc(func, name, base)
    return old_bc(func, name)

import builtins
builtins.__build_class__ = my_bc