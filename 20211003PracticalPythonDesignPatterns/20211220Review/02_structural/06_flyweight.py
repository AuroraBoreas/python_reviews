# 

import json
from typing import Dict, List

class Flyweight:
    def __init__(self, shared_state:str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state:str)->None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'{self.__class__} : shared-> {s} and unique-> {u}')


class FlyweightFactory:
    _flyweights:Dict[str, Flyweight] = {}

    def __init__(self, init_flyweights:Dict) -> None:
        for state in init_flyweights:
            self._flyweights[self.get_state(state)] = Flyweight[state]

    def get_state(self, shared_state:List)->str:
        return '_'.join(sorted(shared_state))

    def get_flyweight(self, shared_state:List)->Flyweight:
        key = self.get_state(shared_state)

        if self._flyweights.get(key):
            print(f'{self.__class__} : {shared_state} not found, creating a new one..')
            self._flyweights[key] = Flyweight[key]
        else:
            print(f'{self.__class__} : reusing the exiting one..')

        return self._flyweights[key]

    def list_flyweights(self)->str:
        print(f'{self.__class__} has {len(self._flyweights)} flyweights:')
        return '\n'.join(self._flyweights.keys())

