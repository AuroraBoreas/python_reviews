"# Python is a protocol orientated language; every top-level function has a dunder method implemented;" 

from typing import Any, Callable, Dict, Tuple, Type, TypeVar
Self = TypeVar('Self')

class BaseMeta(type):
    def __new__(cls:type, name:str, bases:Tuple, body:Dict) -> Type[Self]:
        if bases:
            if Base in bases:
                assert 'bar' in body, f'bar not found in {name}'
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self) -> str:
        return self.bar()