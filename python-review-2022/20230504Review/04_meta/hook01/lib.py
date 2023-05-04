"#" 

from typing import Any, Callable


class Base:
    def foo(self) -> str:
        return self.bar()
    
old_bc = __build_class__

def my_bc(func: Callable, name: str, body: type) -> Any:
    if body:
        if body is Base:
            assert 'bar' in func.__code__.co_names, f'bar not found in {name} class'
            return old_bc(func, name, body)
    return old_bc(func, name, body)

import builtins
builtins.__build_class__ = my_bc