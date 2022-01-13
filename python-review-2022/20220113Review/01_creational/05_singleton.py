# 

from typing import Any, Type


class Singleton:
    class __Singelton:
        def __init__(self) -> None:
            self.val:int = None
        
        def __str__(self) -> str:
            return f'{self!r}, {self.val}'

    instance:__Singelton = None

    def __new__(cls: Type) -> Type:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singelton()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)