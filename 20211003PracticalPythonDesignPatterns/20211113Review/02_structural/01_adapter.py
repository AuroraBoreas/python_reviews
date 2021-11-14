# what i have - adapter - what i want

from typing import Any, Callable


class WhatIhave:
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def required_func(self): pass

class Adapter:
    def __init__(self, wih:WhatIhave, required_func:Callable)->None:
        self.wih = wih
        self.required_func = required_func

    def __getattr__(self, attr:str)->Any:
        return getattr(self.wih, attr)

def client_code()->None:
    a = Adapter(WhatIhave(), WhatIWant.required_func)
    a.wih.provided_func_01()
    a.wih.provided_func_02()
    a.required_func()