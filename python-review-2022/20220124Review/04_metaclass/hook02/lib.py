#"Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

from email.mime import base
from typing import Dict, Tuple, Type


class BaseMeta(type):
    def __new__(cls:Type, name:str, bases:Tuple, body:Dict)->Type:
        if base:
            if Base in bases:
                assert 'bar' in body, f'bar not found in {name}'
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self)->str:
        return self.bar()