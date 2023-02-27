# 

from typing import Any, Self


class Singleton:

    class __Singleton:
        def __init__(self) -> None:
            self.val: int = 1
        def __str__(self) -> str:
            return f"mem_addr={id(self)}, val={self.val}"

    instance: __Singleton = None

    def __new__(cls: type[Self]) -> Self:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr: str) -> Any:
        return getattr(self.instance, attr)

def client_code() -> None:
    s1: Singleton = Singleton()
    s1.val = 1
    s2: Singleton = Singleton()
    s2.val = 2
    print(s1)
    print(s2)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()