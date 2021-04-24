# python is a protocol oriented language

class Base:
    def foo(self):
        return self.bar()


old_bc = __build_class__

def my_bc(func, name, base=None, **kwargs):
    if base:
        if base is Base:
            print('check if bar() method defined') # we can check bar() method here. which is nice;
        return old_bc(func, name, base, **kwargs)
    return old_bc(func, name, **kwargs)

import builtins
builtins.__build_class__ = my_bc
