# 

from typing import Any, Callable


class WhatIHave:
    def provided_func_01(self)->None: pass
    def provided_func_02(self)->None: pass

class WhatIWant:
    def required_func_01(self)->None: pass
    def required_func_02(self)->None: pass

class Adapter:
    def __init__(self, wih:WhatIHave, required_func:Callable) -> None:
        self._wih = wih
        self.func = required_func

    def __getattr__(self, attr:str)->Any:
        return getattr(self._wih, attr)