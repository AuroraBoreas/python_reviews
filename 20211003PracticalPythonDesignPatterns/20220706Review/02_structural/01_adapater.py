# 

from typing import Any, Callable


class WhatIHave:
    def provided_func_01(self) -> None: print(f'{self.__class__} func 01')
    def provided_func_02(self) -> None: print(f'{self.__class__} func 02')

class WhatIWant:
    def required_func_01(self) -> None: print(f'{self.__class__} func 01')
    def required_func_02(self) -> None: print(f'{self.__class__} func 02')

class Adapter:
    def __init__(self, wih:WhatIHave, func:Callable) -> None:
        self._wih = wih
        self.func = func
    
    def __getattr__(self, attr:str) -> Any:
        return getattr(self._wih, attr)

def client_code() -> None:
    w = WhatIHave()
    f = WhatIWant()
    a = Adapter(w, f.required_func_01)
    a.provided_func_01()
    a.func()

if __name__ == '__main__':
    client_code()