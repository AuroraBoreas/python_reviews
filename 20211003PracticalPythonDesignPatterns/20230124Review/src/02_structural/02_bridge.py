from __future__ import annotations
from abc import ABC, abstractmethod


class Abstract:
    def __init__(self, impl: Implementation) -> None:
        self._impl = impl
    def operate(self) -> str:
        return f"{self._impl.__class__}: implemented on platform {self.__class__}"

class ExtendedAbstract(Abstract):
    def operate(self) -> str:
        return f"{self._impl.__class__}: implemented on platform {self.__class__}"

class Implementation(ABC):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return "A"

class ImplementationB(Implementation):
    def do_this(self) -> str:
        return "B"

def main() -> None:
    a1: Abstract = Abstract(ImplementationA())
    print(a1.operate())
    a2: ExtendedAbstract = ExtendedAbstract(ImplementationB())
    print(a2.operate())

if __name__ == '__main__':
    main()
