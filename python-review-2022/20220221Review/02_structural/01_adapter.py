# 

from typing import Any, Callable


class WhatIHave:
    def provided_function_01(self)->None: pass
    def provided_function_02(self)->None: pass

class WhatIWant:
    def required_function_01(self)->None: pass


class Adapter:
    def __init__(self, target:WhatIHave, func:Callable) -> None:
        self._target = target
        self.func    = func

    def __getattr__(self, attr:str)->Any:
        return getattr(self._target, attr)