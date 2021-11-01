# global resource acces

from typing import Any


class Singleton:
    class __Singleton:
        def __init__(self)->None:
            self.val = None

        def __str__(self)->str:
            return '{0!r} {1}'.format(self, self.val)

    instance:__Singleton = None

    def __new__(cls):
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
    s2.val = 'Object val 2'
    print(s2)
    print(s1)
    print(s1 == s2)
    print(s1 is s2)
    