"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

class Base:
    def foo(self):
        return self.bar()

    def __init_subclass__(cls):
        assert hasattr(cls, 'bar'), AttributeError(f'bar not found in {cls}')
        return super().__init_subclass__()