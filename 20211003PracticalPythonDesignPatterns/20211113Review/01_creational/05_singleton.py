# global src access
from typing import Any, TypeVar, Type
_T = TypeVar('_T')

class Singleton:
    class __Singleton:
        def __init__(self)->None:
            self.val: str = None
        def __str__(self)->str:
            return f'{self!r}, {self.val}'

    instance:__Singleton = None

    def __new__(cls: Type[_T]) -> _T:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)

def client_code()->None:
    s1 = Singleton()
    s1.val = 'object val 1'
    print('s1:', s1)

    s2 = Singleton()
    s2.val = 'object val 2'
    print('s2:', s2)
    print('s1:', s1)

if __name__ == '__main__':
    client_code()
