# adapter

from typing import Any, Callable


class WhatIHave:
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def required_func(self): pass

class Adapter:
    def __init__(self, wih:WhatIHave, required_func:Callable) -> None:
        self.wih = wih
        self.required_func = required_func

    def __getattr__(self, attr:str)->Any:
        return getattr(self.wih, attr)

    def execute(self)->None:
        self.wih.provided_func_01()
        self.wih.provided_func_02()
        self.required_func()