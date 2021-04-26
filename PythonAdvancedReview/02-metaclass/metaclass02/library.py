"# python is a protocol orientated lang; \n# every top-level function has a corresponding dunder method implemented" 

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__: ', cls, name, bases, body)
        # interception here to check bar() method in user class
        if bases:
            assert 'bar' in body, "bar() method not found in user class"                
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

