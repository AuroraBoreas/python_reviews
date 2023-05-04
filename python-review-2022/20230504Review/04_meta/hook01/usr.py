"#" 

from lib import Base

class Derived(Base):
    def bar(self) -> str:
        return "bar"
    
class Sibling(Base):
    def operate(self) -> str:
        return "hello"