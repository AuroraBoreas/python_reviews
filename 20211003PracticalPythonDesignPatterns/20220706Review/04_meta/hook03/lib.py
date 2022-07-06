"Python is a protocol orientated lang; every top-level function has a corresponding dunder method;" 


from typing import Any, Callable, Dict, Tuple, Type

class Base:
    def foo(self) -> str:
        return self.bar()

    def __init_subclass__(cls) -> None:
        assert hasattr(cls, 'bar'), f'bar not found in {cls}'
        return super().__init_subclass__()