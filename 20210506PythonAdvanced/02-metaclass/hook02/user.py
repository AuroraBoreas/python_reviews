"#Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

from library import Base

class Derived(Base):
    def bar_(self):
        return 'bar'