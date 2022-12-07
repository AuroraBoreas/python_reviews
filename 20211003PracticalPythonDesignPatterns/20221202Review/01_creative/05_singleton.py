"#" 

from typing import Any


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._val:int = None
        def __str__(self) -> str:
            return f'{self.__class__} : {self._val}'

    __instance:__Singleton = None
    def __new__(cls: type) -> type:
        if not Singleton.__instance:
            Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance

    def __getattr__(self, attr:Any) -> Any:
        return getattr(Singleton.__instance, attr)
    
def client_code() -> None:
    s1 = Singleton()
    s1._val = 1
    s2 = Singleton()
    print(s1)
    print(s2)
    s2._val = 2
    print(s1)
    print(s2)

if __name__ == '__main__':
    client_code()