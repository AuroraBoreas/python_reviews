"#" 

from typing import Any


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._val:int = None
        def __str__(self) -> str:
            return f'{self.__class__} : {self._val}'
    
    sing:__Singleton = None

    def __new__(cls:type) -> type:
        if not Singleton.sing:
            Singleton.sing = Singleton.__Singleton()
        return Singleton.sing

    def __getattr__(self, attr:str) -> Any:
        return getattr(self.sing, attr)

def client_code() -> None:
    s1:Singleton = Singleton()
    s1._val = 1
    s2:Singleton = Singleton()
    s2._val = 2
    print(s1)
    print(s2)

if __name__ == '__main__':
    client_code()