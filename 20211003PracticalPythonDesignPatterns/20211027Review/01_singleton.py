# global src access

from typing import Any

class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = None
        def __str__(self)->str:
            return f'{0!r} {1}'.format(self, self.val)

    instance:__Singleton = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr:str)->Any:
        return getattr(self.instance, attr)

#@ [CSB]
#- C: FAB PS
#- S: ABCD FFP
#- B: CCIM MOSSTV