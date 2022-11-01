"#" 

import json
from typing import Any, Dict, List


class Flyweight:
    def __init__(self, shared:str) -> None:
        self._shared = shared

    def operate(self, unique:str) -> None:
        s = json.dumps(self._shared)
        u = json.dumps(unique)
        print(f'{self.__class__} : shared -> ({s}); unique -> ({u})')

class FlyweightFactory:
    __flyweights:Dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights:List[Any]) -> None:
        for state in init_flyweights:
            self.__flyweights[self.get_state(state)] = Flyweight(state)

    def get_state(self, shared:List[Any]) -> str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared:List[Any]) -> Flyweight:
        key = self.get_state(shared)
        if key not in self.__flyweights:
            print(f'{self.__class__}: {shared} not found, creating a new one..')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print(f'{self.__class__}: using the existing one')
        return self.__flyweights[key]

    def list_flyweight(self) -> None:
        return 'flyweights: \n{}'.format('\n'.join(map(str, self.__flyweights.keys())))

def client_code() -> None:
    ff:FlyweightFactory = FlyweightFactory([['ABC','CBA'], ['EYXZ','zxye'], ['DDD','EEE'], ['ETL','LTE']])
    print(ff.list_flyweight())

if __name__ == '__main__':
    client_code()
