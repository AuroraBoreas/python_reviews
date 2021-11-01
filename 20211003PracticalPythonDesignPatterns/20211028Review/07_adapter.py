# adapter. ABCD FFPS

from typing import Any, Callable

class WhatIHave:
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def required_func(self): pass


class Adapter:
    def __init__(self, what_i_have:WhatIHave, required_func:Callable) -> None:
        self.what_i_have = what_i_have
        self.required_func = required_func

    def __getattr__(self,attr:str)->Any:
        return self.what_i_have(attr)

    def execute(self)->Any:
        self.what_i_have.provoided_func_01()
        self.what_i_have.provoided_func_02()
        self.what_i_have.provoided_func_03()
        self.required_func()

def client_code():
    wih = WhatIHave()
    func = WhatIWant().required_func
    a = Adapter(wih, func)
    a.execute()
