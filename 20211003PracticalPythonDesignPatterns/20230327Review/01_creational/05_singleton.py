# 

from abc import ABC
from typing import Any, Self


class Singleton(ABC):
    class __Singleton:
        def __init__(self) -> None:
            self._val: int = 0x0f
        def __str__(self) -> str:
            return f'{self.__class__} : {self._val}'

    instance: __Singleton = None

    def __new__(cls) -> Self:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr: str) -> Any:
        return getattr(self.instance, attr)