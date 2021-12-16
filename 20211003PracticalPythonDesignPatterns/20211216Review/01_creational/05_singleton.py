# 

from typing import Any, Type


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self.val:int = None

        def __str__(self) -> str:
            return f'{self!r}, {self.val}'

    intance:__Singleton = None

    def __new__(cls: Type) -> Type:
        if not Singleton.intance:
            Singleton.intance = Singleton.__Singleton()
        return Singleton.intance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.intance, attr)