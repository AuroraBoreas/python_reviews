# user.py

from library import Base

"""
context beforehand

Q: how to user if Base class in library.py does have foo() method in the first place?
A: trust?

Q: can we check it before user call it?
A: yes?

Q: wow, how to do it?
A: hint, using keyword "assert"

"""

# check if Base class has foo() method before runtime;
assert hasattr(Base, 'foo'), "Base class has no 'foo' attr!"

class Derived(Base):
    def bar(self):
        return self.foo()
