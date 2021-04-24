# python is a protocol oriented language

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        print('bar' in body)
        if name != 'Base':
            assert 'bar' in body, "bar() not found in user class"
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
