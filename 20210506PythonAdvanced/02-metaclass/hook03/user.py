"#Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

from library import Base

class Derived(Base):
    def _bar(self):
        return 'bar'