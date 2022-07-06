# 

from typing import Any, Type


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._val:int = None

        def __str__(self) -> str:
            return f'{self.__class__} : {self._val}'

    intance: __Singleton = None

    def __new__(cls:Type) -> Type:
        if not Singleton.intance:
            Singleton.intance = Singleton.__Singleton()
        return Singleton.intance

    def __getattr__(self, attr:str) -> Any:
        return getattr(self.intance, attr)

def client_code() -> None:
    s1 = Singleton()
    s1._val = 69
    s2 = Singleton()
    s2._val = 42
    print(s1)
    print(s2)

if __name__ == '__main__':
    client_code()