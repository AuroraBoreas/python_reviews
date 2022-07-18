"Python is a protocol orientated lang; every top-level function has a correspoonding dunder method implemented;" 

from typing import Any, Callable, Dict


class Base:
    def foo(self) -> str:
        return self.bar()

old_bc = __build_class__

def my_bc(func:Callable, name:str, base:Dict) -> Any:
    if base:
        if base is Base:
            return old_bc(func, name, base)
    return old_bc(func, name)

import builtins
builtins.__build_class__ = my_bc