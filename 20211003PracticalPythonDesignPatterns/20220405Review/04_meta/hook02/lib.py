"python is a protocol orientated lang; every high level function has a corresponding dunder method implemented;" 

from typing import Dict, Tuple, Type


class BaseMeta(type):
    def __new__(cls:Type, name:str, bases:Tuple, body:Dict)->type:
        if bases:
            if Base in bases:
                assert 'bar' in body, f'bar not found in {name}'
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self)->str:
        return self.bar()