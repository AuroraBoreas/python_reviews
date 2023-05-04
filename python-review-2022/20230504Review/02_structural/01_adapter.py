"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from typing import Any, Callable

class WhatIHave:
    def func_01(self) -> None: pass
    def func_02(self) -> None: pass

class WhatIWant:
    @staticmethod
    def required_func_01() -> None: pass
    @staticmethod
    def required_func_02() -> None: pass

class Adapter:
    def __init__(self, wih: WhatIHave, func: Callable[..., None]) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._wih, attr)
    
def client_code(a: Adapter) -> None:
    a.func_01()
    a.func()
    a.func_02()

def main() -> None:
    a: Adapter = Adapter(WhatIHave(), WhatIWant.required_func_01)
    client_code(a)

if __name__ == '__main__':
    main()