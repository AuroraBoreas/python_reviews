#"Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Callable, Type, Any

class Base:
    def foo(self)->str: return self.bar()

old_bc = __build_class__

def my_bc(func:Callable, name:str, base:Type=None)->Any:
    if base:
        if Base is base:
            return old_bc(func, name, base)
    return old_bc(func, name)

import builtins
builtins.__build_class__ = my_bc