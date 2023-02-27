# 

import json


class Flyweight:
    def __init__(self, shared: str) -> None:
        self._shared = shared

    def operate(self, unique: str) -> str:
        shared: str = json.dumps(self._shared)
        unique: str = json.dumps(unique)
        return f"{self.__class__} : shared=>({shared}), unique=>({unique})"
    
class FlyweightFactory:
    flyweights: dict[str, Flyweight] = dict()
    
    def __init__(self, init_flyweights: list[str]) -> None:
        for flyweight in init_flyweights:
            self.flyweights[self.get_state(flyweight)] = Flyweight(flyweight)

    def get_state(self, shared: list[str]) -> str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared: list[str]) -> Flyweight:
        key: str = self.get_state(shared)
        if key not in self.flyweights:
            print(f'{self.__class__} : {shared} is not found, creating a new one..')
            self.flyweights[key] = Flyweight(shared)
        else:
            print(f'{self.__class__} : reusing the existing one..')
        return self.flyweights[key]
    
    def show_flyweights(self) -> str:
        return 'flyweights:{}'.format('\n'.join(map(str, self.flyweights.keys())))