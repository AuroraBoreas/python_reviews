# global src access
from typing import Type, TypeVar, Any
T = TypeVar('T')

class Singleton:
    class __Singleton:
        def __init__(self)->None:
            self.val:str = None

        def __str__(self) -> str:
            return f'{self!r}, {self.val}'

    instance:__Singleton = None

    def __new__(cls: Type[T]) -> T:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)

if __name__ == '__main__':
    s1 = Singleton()
    s1.val = 'object val 1'
    print(s1)

    s2 = Singleton()
    s2.val = 'object val 2'
    print(s2)