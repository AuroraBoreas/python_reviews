#"python is a protocol orientated lang; every top-level function has a correpsonding dunder method implemented;" 

from typing import Any, Callable, Dict, Tuple, Type

class Base:
    def foo(self)->str:
        return self.bar()

    def __init_subclass__(cls) -> None:
        assert hasattr(cls, 'bar'), f'bar not found in {cls}'
        super.__init_subclass__()