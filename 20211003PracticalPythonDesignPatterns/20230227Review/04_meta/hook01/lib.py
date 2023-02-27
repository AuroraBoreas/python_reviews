"Python is a protocol orientated language; every top-level function has a corresponding dunder method implemented;" 

class Base:
    def foo(self) -> str:
        return self.bar()
    
old_bc = __build_class__

def my_bc(func, name, base):
    if base:
        if base is Base:
            assert 'bar' in func.__code__.co_names, f'bar not found in {name}'
            return old_bc(func, name, base)
    return old_bc(func, name)

import builtins
builtins.__build_class__ = my_bc