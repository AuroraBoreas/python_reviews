# 

from typing import Callable


class WhatIHave:
    def provided_func_01(self)->None: pass
    def provided_func_02(self)->None: pass

class WhatIWant:
    def required_func_01(self)->None: pass
    def required_func_02(self)->None: pass

class Adapter:
    def __init__(self, wih:WhatIHave, func:Callable) -> None:
        self._wih = wih
        self.func = func
    
    def __getattr__(self, attr:str)->None:
        return getattr(self._wih, attr)