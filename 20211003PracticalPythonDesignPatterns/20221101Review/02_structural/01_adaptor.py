
from typing import Any, Callable

class WhatIHave:
    def func_01(self) -> None: pass
    def func_02(self) -> None: pass

class WhatIWant:
    def required_func_01(self) -> None: pass
    def required_func_02(self) -> None: pass

class Adaptor:
    def __init__(self, wih:WhatIHave, func:Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._wih, attr)

def client_code() -> None:
    a:Adaptor = Adaptor(WhatIHave(), WhatIWant().required_func_01)
    a.func_01()
    a.func()
    a.func_02()

if __name__ == '__main__':
    client_code()