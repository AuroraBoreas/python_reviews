# adapter

from typing import Callable, Any


class WhatIHave:
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def required_func(self): pass

class Adapter:
    def __init__(self, what_i_have:WhatIHave, required_func:Callable)->None:
        self.what_i_have   = what_i_have
        self.required_func = required_func

    def __getatt__(self, attr:str)->Any:
        return getattr(self.what_i_have, attr)