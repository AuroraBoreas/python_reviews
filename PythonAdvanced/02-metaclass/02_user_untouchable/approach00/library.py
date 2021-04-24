# library.py

"""
context beforehand

Q: how to check if user side has bar() method?
A: trust user?

Q: but wait a second. why do u wanna do this in the first place? isn't it insane?
A: library.py designer may abuse power :D

Q: again, do u have any means to check before runtime?
A: yeah. there are typically three approaches
   [*] builtins.__build_class__, i call it "BBC" :^)
   [*] metaclass
   [*] __is_sublcass__

"""

class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__ # capture original build class

def my_bc(*args, **kwargs): # write my own build class
    print('my buildclass ->', args, kwargs)
    return old_bc(*args, **kwargs)

import builtins # import builtins

builtins.__build_class__ = my_bc # swap out
