
from typing import Any, Type, TypeVar
_T = TypeVar('_T')


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self.val:str = None

        def __str__(self) -> str:
            return f'{self!r}, {self.val}'

    instance:__Singleton = None

    def __new__(cls: Type[_T]) -> _T:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)
