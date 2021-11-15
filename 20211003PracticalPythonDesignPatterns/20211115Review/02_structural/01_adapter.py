# whatIhave - adapter - whatIwant 

from typing import Any, Callable


class WhatIHave:
    def provided_func_01(self)->None: pass
    def provided_func_02(self)->None: pass

class WhatIWant:
    def required_func(self)->None: pass

class Adapter:
    def __init__(self, wih:WhatIHave, required_func:Callable) -> None:
        self.wih:WhatIHave = wih
        self.required_func = required_func

    def __getattr__(self, attr:str)->Any:
        return getattr(self.wih, attr)

def client_code()->None:
    a = Adapter(WhatIHave(), WhatIWant.required_func)
    a.wih.provided_func_01()
    a.wih.provided_func_02()
    a.required_func()
