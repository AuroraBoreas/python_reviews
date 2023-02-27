# 

from typing import Any, Callable


class WhatIHave:
    def existed_function_01(self) -> None: print(f"{self.__class__} function 01")
    def existed_function_02(self) -> None: print(f"{self.__class__} function 02")

class WhatIWant:
    def required_function_01(self) -> None: print(f"{self.__class__} function 01")
    def required_function_02(self) -> None: print(f"{self.__class__} function 02")

class Adapter:
    def __init__(self, wih: WhatIHave, func: Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._wih, attr)

def client_code() -> None:
    wih: WhatIHave = WhatIHave()
    func = WhatIWant().required_function_01
    a: Adapter = Adapter(wih, func)
    a.existed_function_01()
    a.func()
    a.existed_function_02()

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()