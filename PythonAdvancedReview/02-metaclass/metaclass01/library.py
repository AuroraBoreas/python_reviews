"# python is a protocol orientated lang; \nevery top-level function has a corresponding dunder method implemented;" 

"""
context

Q: provided that user codebase is not changeable, 
how do library creater ensures that user class Derived has bar() method before runtime?

A: approach01
using "BBC"(builtins.__build_class__)

"""

class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__

# def my_bc(*args, **kwargs):
#     print('BBC: builtins.__build_class__ ->', args, kwargs)
#     return old_bc(*args, **kwargs)

def my_bc(func, name, base=None, **kwargs):
    print(func, name, base, kwargs)
    if base:
        if base is Base:
            # interception here :^)
            print('check bar() method here. func name: ', func.__name__)
            for builtin in dir(func):
                print("\n***{}***".format(builtin))
                if 'bar' in dir(builtin):
                    print('bar() method found!')
                print('bar() method not found')

            # print(dir(func.__code__))
            # assert hasattr(func, 'bar')
        return old_bc(func, name, base, **kwargs)
    return old_bc(func, name, **kwargs)

import builtins
builtins.__build_class__ = my_bc