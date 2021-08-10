"Python is a protocol orientated language, every top-level function has a corresponding dunder method" 

from lib import Base

class Derived(Base):
    def bar(self):
        return 'bar'

class A(Base):
    def a(self):
        return 'a'

    def bar(self):
        return