"Python is a protool orientated lang; every top-level function has a dunder method implemented;" 

from lib import Base

class Derived(Base):
    def bar(self):
        return 'bar'

class A(Base):
    def a(self):
        return 'a'