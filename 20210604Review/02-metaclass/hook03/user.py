"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

from library import Base

class Derived(Base):
    def bar(self)->None:
        return 'bar'

class A(Base):
    def a(self)->None:
        return 'a'