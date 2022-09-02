"Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Callable, Tuple


class Base:
    def foo(self) -> str:
        return self.bar()

"""
def _():
    class Base:
        def foo(self) -> str:
            return 'foo'
    return Base()
"""

old_bc = __build_class__

def my_bc(func:Callable, name:str, base:Tuple=None) -> Any:
    if base:
        if Base is base:
            assert 'bar' in func.__code__.co_names, f'bar not found in {name}'
            return old_bc(func, name)
    return old_bc(func, name, base)

import builtins
builtins.__build_class__ = my_bc