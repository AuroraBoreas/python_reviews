"# Python is a protocol orientated language; every top-level function has a dunder method implemented;" 

from lib import Base

class Derived(Base):
    def bar(self) -> str:
        return 'bar'

class A(Base):
    def buz(self) -> str:
        return 'a'