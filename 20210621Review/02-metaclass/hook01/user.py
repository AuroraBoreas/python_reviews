"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemeneted;" 

from lib import Base

class Derived(Base):
    def bar(self):
        return 'bar'

class A(Base):
    def a(self):
        return 'a'