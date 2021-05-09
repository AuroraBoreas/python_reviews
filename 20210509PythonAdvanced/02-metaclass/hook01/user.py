"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from library import Base

class Derived(Base):
    def bar_(self):
        return 'bar'

    def _bar(self):
        return 'bar'

    def bar(self):
        return 'bar'