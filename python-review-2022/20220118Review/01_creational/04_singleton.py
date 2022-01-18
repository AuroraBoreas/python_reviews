# 

from typing import Any, Type


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self.val:Any = None

        def __str__(self) -> str:
            return f'{self!r}, {self.val}'

    instance:__Singleton = None

    def __new__(cls: type) -> Type:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)