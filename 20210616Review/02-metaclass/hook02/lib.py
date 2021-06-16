"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if bases:
            if Base in bases:
                assert 'bar' in body, f'bar() not found in {name}'
        return super().__new__(cls, name, bases, body)
        
class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()