"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from library import Base

assert hasattr(Base, 'foo'), 'foo() not found in {0}'.format(Base)

class Derived(Base):
    def bar(self):
        return self.foo()