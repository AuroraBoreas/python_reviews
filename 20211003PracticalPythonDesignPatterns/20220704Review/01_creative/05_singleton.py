"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Type


class Singleton:
    class __Singleton: # pimpl idiom
        def __init__(self) -> None:
            self._val:str = None
        def __str__(self) -> str:
            return f'{self.__class__} : {self._val}'

    instance:__Singleton = None

    def __new__(cls:Type) -> Type:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str) -> Any:
        return getattr(self.instance, attr)