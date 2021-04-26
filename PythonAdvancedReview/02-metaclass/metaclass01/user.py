"# python is a protocol orientated lang; \nevery top-level function has a corresponding dunder method implemented;" 

from library import Base

class Derived(Base):
    def bar(self):
        return 'bar'
        