"#" 

from typing import Any


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._val:Any = None
        def __str__(self) -> str:
            return f'{self.__class__} {self._val}'

    instance:__Singleton = None

    def __new__(cls: type) -> __Singleton:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str) -> Any:
        return getattr(self.instance, attr)