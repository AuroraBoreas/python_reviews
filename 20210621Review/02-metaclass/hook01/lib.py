"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemeneted;" 

class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__

def my_bc(func, name, base=None):
    if base:
        if Base is base:
            return old_bc(func, name, base)
    return old_bc(func, name)

import builtins
builtins.__build_class__ = my_bc