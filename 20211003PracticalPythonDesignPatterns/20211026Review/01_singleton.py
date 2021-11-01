# global resource access

from typing import Any

class Singleton:
    class __SingletonObjec:
        def __init__(self):
            self.val = None
        def tostring(self)->str:
            return '{0!r} {1}'.format(self, self.val)

    instance: __SingletonObjec = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__SingletonObjec()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)

if __name__ == '__main__':
    s1 = Singleton()
    s1.val = 'object val 1'
    print(s1.tostring())

    s2 = Singleton()
    s2.val = 'object val 2'
    print(s1.tostring())
    print(s2.tostring())
    print(s1 is s2)