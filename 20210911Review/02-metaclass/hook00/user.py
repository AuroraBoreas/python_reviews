"Python is a protool orientated lang; every top-level function has a dunder method implemented;" 

from lib import Base

assert hasattr(Base, 'foo'), AttributeError(f'foo not found in {Base}')

class Derived(Base):
    def bar(self):
        return self.foo()

class A(Base):
    def a(self):
        return 'a'