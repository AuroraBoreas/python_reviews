"Python is a protocol orientated language; every top-level function has a corresponding dunder method implemented;" 

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if bases:
            if Base in bases:
                assert 'bar' in body, f'bar not found in {name}'
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self) -> str:
        return self.bar()