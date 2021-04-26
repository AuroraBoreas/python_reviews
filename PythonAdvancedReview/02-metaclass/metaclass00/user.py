# Python is a protocol orientated lang
# every top-level function has a corresponding dunder method implemented

"""
# context

Q: given that "library.py" class Base is not changable by user;
how do user guarantee that class Base has foo() method before runtime?

A: assert hasattr(Base, 'foo')

"""

from library import Base 

assert hasattr(Base, 'foo'), "Library messed up"

class Derived(Base):
    def bar(self):
        return self.foo()