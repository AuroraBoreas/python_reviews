from typing import Any, Callable

class Base:
    def foo(self) -> str:
        return self.bar()

    def __init_subclass__(cls) -> None:
        assert hasattr(cls, 'bar'), f'bar not found int {cls}'
        super().__init_subclass__()
