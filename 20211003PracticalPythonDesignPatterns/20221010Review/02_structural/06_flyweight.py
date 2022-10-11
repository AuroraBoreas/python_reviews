#

from typing import Dict, List
import json

class Flyweight:
    def __init__(self, shared:str) -> None:
        self._shared = shared

    def operate(self, unique:str) -> None:
        s = json.dumps(self._shared)
        u = json.dumps(unique)
        return f'{self.__class__} : shared -> {s}; unique -> {u}'

class FlyweightFactory:
    flyweights:Dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights:List) -> None:
        for status in init_flyweights:
            self.flyweights[self.get_status(status)] = Flyweight(status)
    
    def get_status(self, shared:List) -> str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared:List) -> Flyweight:
        key = self.get_status(shared)

        if key not in self.flyweights:
            print(f'{self.__class__} : {shared} not found; create a new instead')
            self.flyweights[key] = Flyweight(shared)
        else:
            print(f'{self.__class__} : using the exiting one')
        return self.flyweights[key]

    def list_flyweights(self) -> None:
        return 'flyweights:\n{}'.format('\n'.join(map(str, self.flyweights.keys())))