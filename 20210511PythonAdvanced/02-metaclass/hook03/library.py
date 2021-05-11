"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('__new__ : ', cls, name, bases, body)
        if bases:
            if not 'bar' in body:
                raise AttributeError("bar() not found in user class!")
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()