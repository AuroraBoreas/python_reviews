#"python is a protocol orientated lang; every top-level function has a correpsonding dunder method implemented;" 

from lib import Base

class Derived(Base):
    def bar(self)->str:
        return 'bar'

class A(Base):
    def a(self)->str:
        return 'a'