#"python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Type


class Base:
    def foo(self)->str:
        return self.bar()

    def __init_subclass__(cls:Type) -> None:
        assert hasattr(cls, 'bar'), f'bar not found in {cls}'
        return super().__init_subclass__()