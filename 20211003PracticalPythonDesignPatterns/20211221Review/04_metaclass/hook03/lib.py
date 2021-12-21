#"Python is a protocol orientated lang; every top-level function has a corresponding dunder methond implemented;" 


class Base:
    def foo(self)->str:
        return self.bar()

    def __init_subclass__(cls) -> None:
        assert hasattr(cls, 'bar'), f'bar not found in {cls}'
        super().__init_subclass__()