#"python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Callable


class Base:
    def foo(self)->str:
        return self.bar()

old_bc = __build_class__

def my_bc(func:Callable, name:str, base:type=None)->Any:
    print(f'__build_class__ : {func}, {name}, {base}')
    if base:
        if Base is base:
            assert 'bar' in func.__code__.co_names, f'bar not found in {name}'
            return old_bc(func, name)
    return old_bc(func, name, base)

import builtins
builtins.__build_class__ = my_bc