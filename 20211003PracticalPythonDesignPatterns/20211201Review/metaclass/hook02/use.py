#"python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from lib import Base

class Derived(Base):
    def bar(self)->str:
        return self.foo()

class A(Base):
    def a(self)->str:
        return 'a'