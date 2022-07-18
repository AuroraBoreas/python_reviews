"Python is a protocol orientated lang; every top-level function has a correspoonding dunder method implemented;" 

from typing import Dict, Tuple

class BaseMeta(type):
    def __new__(cls:type, name:str, bases:Tuple, body:Dict) -> type:
        if bases:
            if Base in bases:
                assert 'bar' in body, f'bar not found in {name}'
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self) -> str:
        return self.bar()