"#Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__

def my_bc(*args, **kwargs):
    print('__build_class : ', args, kwargs)
    return old_bc(*args, **kwargs)

import builtins

builtins.__build_class__ = my_bc