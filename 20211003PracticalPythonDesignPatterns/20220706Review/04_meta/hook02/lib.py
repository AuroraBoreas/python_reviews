"Python is a protocol orientated lang; every top-level function has a corresponding dunder method;" 


from typing import Any, Callable, Dict, Tuple, Type

class BaseMeta(type):
    def __new__(cls:Type, name:str, bases:Tuple, body:Dict) -> Type:
        if bases:
            if Base in bases:
                assert 'bar' in body, f'bar not found in {name}'
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self) -> str:
        return self.bar()