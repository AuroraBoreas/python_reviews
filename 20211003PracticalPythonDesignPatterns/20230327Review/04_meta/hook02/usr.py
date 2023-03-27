# 

from lib import Base

class Derived(Base):
    def bar(self) -> str:
        return 'bar'
    
class A(Base):
    def a(self) -> str:
        return 'a'