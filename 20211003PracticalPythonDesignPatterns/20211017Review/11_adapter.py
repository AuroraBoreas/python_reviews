# adapter

from typing import Any, Callable

class WhatIHave:
    def provided_func_01(self) -> Any: pass
    def provided_func_02(self) -> Any: pass

class WhatIWant:
    def required_func(self) -> Any: pass


class Adapter:
    def __init__(self, what_i_have:WhatIHave, required_func:Callable) -> None:
        self.what_i_have = what_i_have
        self.required_func = required_func

    def __getattr__(self, attr:str) -> Any:
        return getattr(self.what_i_have, attr)

if __name__ == '__main__':
    a = Adapter(WhatIHave(), getattr(WhatIWant(), 'required_func'))
    a.what_i_have.provided_func_01()
    a.what_i_have.provided_func_02()
    a.required_func()