"Python is a protocol orientated language; every top-level function has a corresponding dunder method implemented" 

from typing import Type


class Base:
    def foo(self) -> str:
        return self.bar()

    def __init_subclass__(cls: Type) -> None:
        assert hasattr(cls, 'bar'), f'bar not found in {cls}'
        super().__init_subclass__()