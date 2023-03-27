# 

from typing import Callable, Type


class Base:
    def foo(self) -> str:
        return self.bar()
    
old_bc = __build_class__

def new_bc(func: Callable, name: str, base: Type):
    if base:
        if Base is base:
            assert 'bar' in func.__code__.co_names, f'bar not found in {name}'
            return old_bc(func, name)
    return old_bc(func, name, base)

import builtins
builtins.__build_class__ = new_bc