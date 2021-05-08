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

import dis
def my_bc(*args, **kwargs):
    print('__build_class__ : ', args, kwargs)
    # print(dis.dis(args[0]))
    # print(args[0].__code__.co_names)
    # print(dir(args[0].__code__))
    return old_bc(*args, **kwargs)

def my_bc2(func, name, base=None):
    # print('__build_class__ : ', func, name, base)
    if base is None:
        return old_bc(func, name)
    if not 'bar' in func.__code__.co_names:
        raise AttributeError("bar() not found in user class!")
    return old_bc(func, name, base)

import builtins
builtins.__build_class__ = my_bc2