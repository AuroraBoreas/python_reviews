"python is a protocol orientated lang; every high level function has a corresponding dunder method implemented;" 

from lib import Base

class Derived(Base):
    def bar(self)->str:
        return 'bar'

class A(Base):
    def a(self)->str:
        return 'a'