"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from ast import Dict
import json


class Flyweight:
    def __init__(self, shared: str) -> None:
        self._shared = shared

    def operate(self, unique: str) -> str:
        s: str = json.dumps(self._shared)
        u: str = json.dumps(unique)
        return f"{self.__class__}: shared -> {s}, unique -> {u}"
    
class FlyweightFactory:
    flyweights: Dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights: list[list[str]]) -> None:
        for flyweight in init_flyweights:
            self.flyweights[self.get_state(flyweight)] = Flyweight(flyweight)
    
    def get_state(self, shared: list[str]) -> str:
        return ''.join(sorted(shared))
    
    def get_flyweight(self, shared: list[str]) -> Flyweight:
        key: str = self.get_state(shared)
        if not key in self.flyweights:
            print(f"{self.__class__}: flyweight({shared}) not found, creating a new one...")
            self.flyweights[key] = Flyweight(shared)
        else:
            print(f"{self.__class__}: resuing the existed one")
        return self.flyweights[key]
    
    def display(self) -> str:
        return "flyweight list: {0}".format('\n'.join(map(str, self.flyweights.keys())))
