from lib import Base

assert hasattr(Base, "foo"), f"foo not found in {Base}"

class Derived1(Base):
    def bar(self) -> str:
        return self.foo()
