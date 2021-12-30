#"Python is a protocol orietated lang; every top-level function has a dunder method implemented;" 

from lib import Base

class Derived(Base):
    def bar(self)->str:
        return 'bar'

class A(Base):
    def a(self)->str:
        return 'a'