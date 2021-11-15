# flyweight objects contain intrinsic fields only; extrinsic fields are passed in as external objects 

import json
from typing import Dict

class Flyweight:
    def __init__(self, shared_state:str) -> None:
        self._shared_state = shared_state
    
    def operation(self, unique_state:str)->None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'{self.__class__}: shared->({s}), unique->({u})')

class FlyweightFactory:
    _flyweights:Dict[str, Flyweight] = {}

    def __init__(self, init_flyweights:Dict) -> None:
        for state in init_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, shared_state:Dict)->str:
        return '_'.join(sorted(shared_state))

    def get_flyweight(self, shared_state:Dict)->Flyweight:
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print(f'\n{self.__class__}: {shared_state} not found, creating a new one..')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f'\n{self.__class__}: reusing existing one..')
        return self._flyweights[key]

    def list_flyweight(self)->None:
        print(f'{self.__class__}: i have {len(self._flyweights)} flyweights')
        print('\n'.join(map(str, self._flyweights.keys())))

def client_code()->None:
    ff = FlyweightFactory([
        list('abc'),
        list('abd'),
        list('123'),
    ])
    ff.list_flyweight()

    flyweight = ff.get_flyweight(list('abe'))
    flyweight.operation(['cy', 'zhangliang'])

    ff.list_flyweight()

if __name__ == '__main__':
    client_code()