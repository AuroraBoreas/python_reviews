"python is a protocol orientated lang; every high level function has a corresponding dunder method implemented;" 

from lib import Base

assert hasattr(Base, 'foo'), f'foo not found in {Base}'

class Derived(Base):
    def bar(self)->str:
        return self.foo()