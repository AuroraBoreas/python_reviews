"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Callable


class Base:
    def foo(self) -> str:
        return self.bar()

old_bc = __build_class__

def my_bc(func:Callable, name:str, base:type=None) -> Any:
    print(func, name, base, sep=' - ')
    if base:
        if Base is base:
            # print(func, name, base)
            assert 'bar' in func.__code__.co_names, f'bar not found in {name}'
            return old_bc(func, name, base)
    return old_bc(func, name)

import builtins
builtins.__build_class__ = my_bc