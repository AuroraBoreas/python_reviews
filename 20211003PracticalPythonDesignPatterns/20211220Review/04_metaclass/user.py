#"Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

from lib import Base

assert hasattr(Base, 'foo'), f'foo not found in {Base}'


class Derived(Base):
    def bar(self)->str: 
        return self.foo()

class A(Base):
    def a(self)->str:
        return 'a'