from lib import Base

class Derived1(Base):
    def bar(self) -> str:
        return 'bar'

class Derived2(Base):
    def a(self) -> str:
        return 'a'
