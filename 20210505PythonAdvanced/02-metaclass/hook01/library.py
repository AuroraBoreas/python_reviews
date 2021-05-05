"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

class Base:
    def foo(self):
        return self.bar()


"""
```Python

def func():
    class TS:
        def foo(self):
            return 'foo'

import dis

dis.dis(func)
```
"""

old_bc = __build_class__

def my_bc(*args, **kwargs):
    print('__build_class__ : ', args, kwargs)
    return old_bc(*args, **kwargs)

import builtins
builtins.__build_class__ = my_bc