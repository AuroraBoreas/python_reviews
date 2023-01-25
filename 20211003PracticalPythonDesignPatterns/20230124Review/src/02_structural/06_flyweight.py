
import json
from typing import Any


class Flyweight:
    def __init__(self, shared: str) -> None:
        self._shared = shared

    def operate(self, unique: str) -> str:
        s: str = json.dumps(self._shared)
        u: str = json.dumps(unique)
        return f"{self.__class__}: shared -> ({s}), unique -> ({u})"

class FlyweightFactory:
    flyweights: dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights: list[Any]) -> None:
        for flyweight in init_flyweights:
            self.flyweights[self.get_status(flyweight)] = Flyweight(flyweight)

    def get_status(self, shared: list[Any]) -> str:
        return ''.join(sorted(shared))

    def get_flyweight(self, shared: list[Any]) -> Flyweight:
        key: str = self.get_status(shared)
        if key not in self.flyweights:
            print(f"{self.__class__}: {shared} not found, creating a new one..")
            self.flyweights[key] = Flyweight[key]
        else:
            print(f"{self.__class__}: reusing the existed one.")
        return self.flyweights[key]

    def display_flyweights(self) -> str:
        return "flyweight factory:\n {0}".format("\n".join(self.flyweights.keys()))

