"#" 
from typing import Callable, Any

class WhatIWant:
    def required_func_01(self) -> None:
        ...

    def required_func_02(self) -> None:
        ...

class WhatIHave:
    def existed_func_01(self) -> None:
        ...

    def existed_func_02(self) -> None:
        ...

class Adapter:
    def __init__(self, wih: WhatIHave, func: Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._wih, attr)
