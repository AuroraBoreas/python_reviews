"""
@ what
__slots__

@ why
by default, Python compiler utilizes dict to collect all attributes of class; 
we can edit arbitrary attributes at run-time;

if we created thounds and millions of objects by a large scale,
this mechnism will eat lots of RAM

@ how
using __slots__ to address this problem

__slots__ tells compiler to allocate space for a fixed set of attributes

"""

from typing import Any

class A:
    def __init__(self, name: str, identifier: Any):
        self.name = name
        self.identifier = identifier

class B:
    __slots__ = ('name', 'identifier')

    def __init__(self, name: str, identifier: Any):
        self.name = name
        self.identifier = identifier
        self.first = 0
        self.last = 69