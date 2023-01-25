
from typing import Any, Self


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._values: list[int] = list()
        def __str__(self) -> str:
            return f"values: {', '.join(map(str, self._values))}"

    instance: __Singleton = None

    def __new__(cls: type[Self]) -> __Singleton:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr: str) -> Any:
        return getattr(self.instance, attr)

def client_code() -> None:
    s1 = Singleton()
    s1._values.extend([1, 2])
    print(s1)
    s2 = Singleton()
    s2._values = [3, 4]
    print(s1)
    print(s2)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()
