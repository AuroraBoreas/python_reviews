"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

class Base:
    def foo(self):
        return self.bar()

"""

```Python

import dis

def func():
    class TS:
        def foo(self):
            return 'foo'


dis.dis(func)

```


```STACK

__CREATE_FUNC__

__CREATE_OBJ__

__BUILD_CLASS__

```

"""

old_bc = __build_class__

def my_bc(*args, **kwargs):
    print('__build_class__ : ', args, kwargs)
    return old_bc(*args, **kwargs)


import builtins

builtins.__build_class__ = my_bc