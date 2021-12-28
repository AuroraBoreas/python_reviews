# 

from typing import Any, Callable


class WhatIHave:
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def required_func_01(self): pass
    def required_func_02(self): pass

class Adapter:
    def __init__(self, wih:WhatIHave, func:Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr:str)->Any:
        return getattr(self._wih, attr)