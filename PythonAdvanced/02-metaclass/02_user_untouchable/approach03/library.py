# python is a protocol oriented lang

class Base:
    def foo(self):
        return self.bar()
    def __init_subclass__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        assert hasattr(cls, 'bar'), "user class fucked"
        super().__init_subclass__(**kwargs)
