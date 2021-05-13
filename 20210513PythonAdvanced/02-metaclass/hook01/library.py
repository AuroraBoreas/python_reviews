"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

class Base:
    def foo(self):
        return self.bar()


old_bc = __build_class__

def my_bc(func, name, base=None):
    print('__build_class__ : ', func, name, base)
    if base:
        if Base is base:
            if not 'bar' in func.__code__.co_names:
                raise AttributeError('bar() not found in user class!')
    return old_bc(func, name, base)

import builtins
builtins.__build_class__ = my_bc