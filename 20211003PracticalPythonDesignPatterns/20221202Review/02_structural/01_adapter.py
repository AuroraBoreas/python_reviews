"#"


from typing import Any, Callable


class WhatIHave:
    def existed_func01(self) -> Any: pass
    def existed_func02(self) -> Any: pass

class WhatIWant:
    def required_func01(self) -> Any: pass
    def required_func02(self) -> Any: pass

class Adapter:
    def __init__(self, wih:WhatIHave, func:Callable) -> None:
        self._wih:WhatIHave = wih
        self._func:Callable = func

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._wih, attr)

def client_code() -> None:
    a1:Adapter = Adapter(WhatIHave(), WhatIWant().required_func01)
    a1.existed_func01()
    a1._func()
    a1.existed_func02()

if __name__ == '__main__':
    client_code()