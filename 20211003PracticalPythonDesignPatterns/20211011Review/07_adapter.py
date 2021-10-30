
from typing import Callable, Any

class WhatIHave:
    def provided_func_01(self):
        pass

    def provided_func_02(self):
        pass

class WhatIWant:
    def required_func(self):
        pass


class Adapter:
    def __init__(self, whatihave:WhatIHave, required_func:Callable)->None:
        self.whatihave = whatihave
        self.required_func = required_func

    def required_func(self):
        self.whatihave.provided_func_01()
        self.whatihave.provided_func_02()
        self.required_func()

    def __getattr__(self, attr:str)->Any:
        return getattr(self.whatihave, attr)
