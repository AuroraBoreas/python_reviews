# 
from __future__ import annotations
from typing import Any, List


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._vals:List[Any] = []
        def __str__(self) -> str:
            return f'{self._vals}'

    singleob:__Singleton = None

    def __new__(cls: type) -> Singleton:
        if not Singleton.singleob:
            Singleton.singleob = Singleton.__Singleton()
        return Singleton.singleob

    def __getattr__(self, attr:str) -> Any:
        return getattr(self.singleob, attr)